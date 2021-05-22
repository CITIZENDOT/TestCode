import click
import os
import subprocess
import fnmatch
import tempfile
from rich.text import Text
from rich import print as rprint
from rich.table import Table
from rich.live import Live


def add_options(options):
    def _add_options(func):
        for option in reversed(options):
            func = option(func)
        return func

    return _add_options


def get_testcases(input, output):
    """
    Returns list of files, which have common names in INPUT_DIR and OUTPUT_DIR
    """
    input_files = set(os.listdir(input))
    output_files = set(os.listdir(output))
    common_files = sorted(
        list(input_files & output_files), key=lambda x: os.path.basename(x)
    )
    return common_files


__options = [
    click.option(
        "-S",
        "--source",
        default="main.cpp",
        type=click.Path(exists=True, resolve_path=True, readable=True),
        help="Path to source code. Extension should be either .c or .cpp",
        show_default=True,
    ),
    click.option(
        "-I",
        "--input",
        default="Input",
        type=click.Path(exists=True, resolve_path=True),
        help="Input directory for test-cases",
        show_default=True,
    ),
    click.option(
        "-O",
        "--output",
        default="Output",
        type=click.Path(exists=True, resolve_path=True),
        help="Output directory for test-cases",
        show_default=True,
    ),
    click.option(
        "-T",
        "--timeout",
        type=click.IntRange(min=1),
        default=2,
        help="Time Limit for each testcase",
        show_default=True,
    ),
]


@click.group()
def cli():
    pass


@cli.command()
@add_options(__options)
def checkenv(source, input, output, timeout):
    """Prints Input, Output directory paths, Source file path"""

    error_style = "red bold"
    success_style = "green"

    table = Table()
    table.add_column("Property")
    table.add_column("Value")

    table.add_row("source", Text(os.path.relpath(source), style=success_style))
    table.add_row("input", Text(os.path.relpath(input), style=success_style))
    table.add_row("output", Text(os.path.relpath(output), style=success_style))
    table.add_row("timeout", Text(str(timeout) + " seconds", style=success_style))

    table.header_style = "cyan bold"
    rprint(table)


@cli.command()
@add_options(__options)
def verify(source, input, output, timeout):
    """Runs the code against all the valid input test-cases"""

    COMPILER = "g++"
    OUTPUT_EXECUTABLE = tempfile.NamedTemporaryFile(mode="w").name
    OUTPUT_FILE = tempfile.NamedTemporaryFile(mode="w").name
    SUCCESS_STYLE = "green"
    ERROR_STYLE = "bold red"

    source_name, source_ext = os.path.splitext(source)
    if source_ext.lower() == "c":
        COMPILER = "gcc"

    is_not_compiled = subprocess.call(
        [COMPILER, source, "-o", OUTPUT_EXECUTABLE], stderr=open(OUTPUT_FILE, "w")
    )

    if is_not_compiled:
        rprint(Text("❌ Compilation Failed", style="bold red"))
        return -1

    test_cases = get_testcases(input, output)

    table = Table(title=f"Results - {os.path.basename(source)}")
    table.add_column("Testcase Name")
    table.add_column("Verdict")

    with Live(table, auto_refresh=False) as live:
        for i, file_name in enumerate(test_cases):
            is_TLE = False
            OUTPUT_FILE = tempfile.NamedTemporaryFile(mode="w").name
            try:
                subprocess.call(
                    [OUTPUT_EXECUTABLE],
                    stdin=open(os.path.join(input, file_name)),
                    stdout=open(OUTPUT_FILE, "w"),
                    timeout=timeout,
                )
            except subprocess.TimeoutExpired:
                is_TLE = True
                table.add_row(
                    file_name,
                    Text("❌ Time Limit Exceeded", ERROR_STYLE),
                )
            if is_TLE:
                live.update(table, refresh=True)
                continue

            with open(OUTPUT_FILE) as f:
                output_str = f.read().strip().splitlines()

            with open(os.path.join(output, file_name)) as f:
                true_output_str = f.read().strip().splitlines()

            if len(output_str) != len(true_output_str):
                table.add_row(
                    file_name,
                    Text("❌ No. of lines do not match", ERROR_STYLE),
                )
                live.update(table, refresh=True)
                continue

            for j, line in enumerate(output_str):
                if line.strip() != true_output_str[j].strip():
                    table.add_row(
                        file_name,
                        Text(f"❌ Mismatch at line {j + 1}", ERROR_STYLE),
                    )
                    live.update(table, refresh=True)
                    continue

            table.add_row(file_name, Text("✔ Passed!", SUCCESS_STYLE))
            os.remove(OUTPUT_FILE)
        os.remove(OUTPUT_EXECUTABLE)
