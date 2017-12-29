# py3-cli-template
A simple template for creating a Python CLI tool that reads line-delimited data from files or standard input. 

```text
$ ./cli.py -h

usage: cli.py [-h] [-d] [-v] [--version] [FILE [FILE ...]]

A simple template for creating a Python CLI tool that reads 
line-delimited data from files or standard input.

positional arguments:
  FILE           files to read, if empty, stdin is used

optional arguments:
  -h, --help     show this help message and exit
  -d, --debug    Print Logging Level DEBUG or higher
  -v, --verbose  Print Logging Level INFO or higher
  --version      show program's version number and exit

Usage:
    $ ./cli.py file1.csv
    $ ./cli.py file1.csv file2.csv 
    $ cat file1.csv | ./cli.py
```
