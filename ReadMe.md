## Test your Code before you Submit!

This repo mainly aims to automate code testing, before your submission. If test cases are small enough, This repo is not for you.

Sometimes test cases are large (in order of 10000...), which are not possible to test manually and check whether the output is correct.

## Usage:

Copy your source code into `main.c`.
Now, Collect your large testcases. Place them in `Input` and `Output` folders. And name them in such a way that, both file names are same. 
For example, Input for a test case is named as 1.txt and placed in Input folder. So, Output for that corresponing Input should be named as 1.txt and should be placed in Output folder.

_Did this seem complicated to you? Do you have any other ways for this? If yes, Open an Issue or Make a Pull Request_

##### Please Note that source code and testcase folders can be anywhere, Specify corresponing arguments and path to it and you're good to go.

```bash
$ python3 main.py -h
usage: main.py [-h] [-L {c,cpp}] [-S SRC] [-I INPUT_DIR] [-O OUTPUT_DIR] [-T TIMEOUT]

C/C++ Code Testing

optional arguments:
  -h, --help            show this help message and exit
  -L {c,cpp}, --language {c,cpp}
                        Choose your language (default: c)
  -S SRC, --source SRC  Source Code (default: main.c)
  -I INPUT_DIR, --input INPUT_DIR
                        Input folder for testcases (default: Input)
  -O OUTPUT_DIR, --output OUTPUT_DIR
                        Output folder for testcases (defualt: Output)
  -T TIMEOUT, --timeout TIMEOUT
                        Time Out (default: 2 Seconds)
```

#### Sample Directory Structure
```bash
.
├── Input
│   ├── 1.txt
│   ├── 2
│   ├── 4.txt
│   └── testcase3.txt
├── main.cpp
├── main.py
├── Output
│   ├── 1.txt
│   ├── 2
│   ├── 4.txt
│   └── testcase3.txt
└── ReadMe.md
```

#### Examples

* Consider given code and testcases in this repo.
```bash
python3 main.py -L cpp -S main.cpp
```
---
* If source code is at `~/Documents/prob.c` and testcase folders are at `~/Desktop/prob/Input` and `~/Desktop/prob/Output` (for Input and Output respectively).
```bash
python3 main.py -S ~/Documents/prob.c -I ~/Desktop/prob/Output -O ~/Desktop/prob/Output
```

A sample C++ Code and 4 testcases are given. Feel free to modify it for your requirements.

**Star this repo, If you feel it's worthy!**