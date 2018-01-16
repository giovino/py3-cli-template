# py3-cli-template
A simple template for creating a Python CLI tool that reads line-delimited data from files or standard input. 

```text
$ ./cli.py -h
usage: cli.py [-h] [--csv] [--delimiter DELIMITER] [--json] [-v] [-d]
              [--version]
              [FILE [FILE ...]]

A simple template for creating a Python CLI tool that reads 
line-delimited, CSV or JSON Lines formatted data from files 
or standard input.

positional arguments:
  FILE                  files to read, if empty, stdin is used

optional arguments:
  -h, --help            show this help message and exit
  --csv                 read CSV formatted file
  --delimiter DELIMITER
                        character used to separate csv fields
  --json                read JSON Lines formatted file
  -v, --verbose         Print Logging Level INFO or higher
  -d, --debug           Print Logging Level DEBUG or higher
  --version             show program's version number and exit

Usage:
    $ ./cli.py file1.txt
    $ ./cli.py file2.csv --csv
    $ ./cli.py file2.csv --csv --delimiter="|"
    $ ./cli.py file3.jsonl --json
    $ cat file1.csv | ./cli.py --csv
```
