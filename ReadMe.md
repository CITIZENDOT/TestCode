## Test your Code before you Submit!

This repo mainly aims to automate code testing, before your submission. If test cases are small enough, This repo is not for you.

Sometimes test cases are large (in order of 10000...), which are not possible to test manually and check whether the output is correct.

## Usage:

Copy your source code into `main.c`.
Now, Collect your large testcases. Place them in `Input` and `Output` folders. And name them in such a way that, both file names are same. 
For example, Input for a test case is named as 1.txt and placed in Input folder. So, Output for that corresponing Input should be named as 1.txt and should be placed in Output folder.

**_Did this seem complicated to you? Do you have any other ways for this? If yes, Open an Issue or Make a Pull Request_**

```bash
$ python3 main.py -h
usage: main.py [-h] [-I INPUT_DIR] [-O OUTPUT_DIR] [-T TIMEOUT]

C Code Testing

optional arguments:
  -h, --help            show this help message and exit
  -I INPUT_DIR, --input INPUT_DIR
                        Input Directory (default: Input)
  -O OUTPUT_DIR, --output OUTPUT_DIR
                        Output Directory (defualt: Output)
  -T TIMEOUT, --timeout TIMEOUT
                        Time Out

```

#### Sample Directory Structure
```bash
.
├── Input
│   ├── 1
│   ├── 2
│   ├── 3
│   ├── 4
│   ├── 5
│   ├── 6
│   ├── 7
│   ├── 8
│   └── 9
├── main.c
├── main.py
├── Output
│   ├── 1
│   ├── 2
│   ├── 3
│   ├── 4
│   ├── 5
│   ├── 6
│   ├── 7
│   ├── 8
│   └── 9
└── ReadMe.md
```

A sample C Code and 9 testcases are given. Feel free to modify for your requirements.

**Star this repo, If you feel it's worthy!**