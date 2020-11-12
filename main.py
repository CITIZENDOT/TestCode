import os
import subprocess
import fnmatch
import argparse
try:
    from colorama import Fore, Style
    LIGHTWHITE_EX = Fore.LIGHTWHITE_EX
    GREEN = Fore.GREEN
    RED = Fore.RED
    LIGHTCYAN_EX = Fore.LIGHTCYAN_EX
    LIGHTYELLOW_EX = Fore.LIGHTYELLOW_EX
    BRIGHT = Style.BRIGHT
    RESET_ALL = Style.RESET_ALL
except ModuleNotFoundError:
    LIGHTWHITE_EX = ''
    GREEN = ''
    RED = ''
    LIGHTCYAN_EX = ''
    LIGHTYELLOW_EX = ''
    BRIGHT = ''
    RESET_ALL = ''
    


def get_testcases(INPUT_DIR, OUTPUT_DIR):
    """
    Returns list of files, which have common names in INPUT_DIR and OUTPUT_DIR
    """
    input_files = set(os.listdir(INPUT_DIR))
    output_files = set(os.listdir(OUTPUT_DIR))
    common_files = list(input_files & output_files)
    return common_files

def print_banner(SRC, testcases_count):
    print("=" * 50)
    print(f"{LIGHTYELLOW_EX}{BRIGHT}Source: {SRC}{RESET_ALL}")
    print(f"{LIGHTWHITE_EX}{BRIGHT}Number of TestCases: {GREEN}{testcases_count}")


def print_testcase(number):
    print(
        f"{LIGHTCYAN_EX}Test Case {number}{RESET_ALL}".ljust(30) + ":  ",
        end='',
    )

def print_error_message(message):
    print(f"{RED}{BRIGHT}{message}{RESET_ALL}")


def print_success_message(message):
    print(f"{GREEN}{BRIGHT}{message}{RESET_ALL}")


parser = argparse.ArgumentParser(description="C/C++ Code Testing")
parser.add_argument('-L', '--language', type=str, dest='LANG',
                    help='Choose your language (default: c)', choices=['c', 'cpp'], default='c')
parser.add_argument('-D', '--sorce-directory', type=str, dest='SRC_DIR',
                    help='Source Directory')
parser.add_argument('-N', '--pattern', type=str, dest='PATTERN',
                    help='Name/Pattern of Source Code in Directory')
parser.add_argument('-I', '--input', type=str, dest='INPUT_DIR',
                    help='Input folder for testcases')
parser.add_argument('-O', '--output', type=str, dest='OUTPUT_DIR',
                    help='Output folder for testcases')
parser.add_argument('-T', '--timeout', type=float,
                    dest='TIMEOUT', help='Time Out (Default =  5 Seconds)', default=5)
args = parser.parse_args()


def test(SRC, LANG, INPUT_DIR, OUTPUT_DIR, TIMEOUT):
    OUTPUT_FILE = '.output'
    test_cases = get_testcases(INPUT_DIR, OUTPUT_DIR)
    print_banner(SRC, len(test_cases))

    if LANG == "c":
        compiler = "gcc"
    else:
        compiler = "g++"
    is_not_compiled = subprocess.call([compiler, SRC, "-o", "a.out"],
                                      stderr=open(OUTPUT_FILE, 'w'))
    if (is_not_compiled):
        print_error_message("Compilation Error")
        os.remove(OUTPUT_FILE)
        exit(1)
    for i in range(len(test_cases)):
        file_name = test_cases[i]
        try:
            subprocess.call(["./a.out"],
                            stdin=open(os.path.join(INPUT_DIR, file_name), 'r'), stdout=open(OUTPUT_FILE, 'w'), timeout=TIMEOUT)
            print_testcase(file_name)
        except subprocess.TimeoutExpired:
            print_testcase(file_name)
            print_error_message("Time Limit Exceeded")
            continue
        with open(os.path.join(OUTPUT_DIR, file_name), 'r') as f:
            output = f.read()
        with open(OUTPUT_FILE, 'r') as f:
            submission = f.read()
        output = output.strip().splitlines()
        submission = submission.strip().splitlines()
        if (len(output) != len(submission)):
            print_error_message("Wrong Output (No. of lines didn't match)")
            continue
        for j in range(len(output)):
            if (output[j].strip() != submission[j].strip()):
                print_error_message("Wrong Output")
                break
        else:
            print_success_message("Passed!")
    os.remove(OUTPUT_FILE)
    os.remove('a.out')
    print("=" * 50, end='\n\n')


def main(SRC_DIR, PATTERN, LANG, INPUT_DIR, OUTPUT_DIR, TIMEOUT):
    for root, dirname, filename in os.walk(SRC_DIR):
        matches = fnmatch.filter(filename, PATTERN)
        for match in matches:
            test(os.path.join(root, match), LANG,
                 INPUT_DIR, OUTPUT_DIR, TIMEOUT)


if __name__ == "__main__":
    main(args.SRC_DIR, args.PATTERN, args.LANG,
         args.INPUT_DIR, args.OUTPUT_DIR, args.TIMEOUT)
