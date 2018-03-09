# py3-cli-template
A simple template for creating a Python CLI tool that reads line-delimited data from files or standard input. 

```text
usage: cli.py [-h] [-if INPUT_FORMAT] [-id DELIMITER] [-o [OUTPUT_FILENAME]]
              [-v] [-d] [--version]
              [FILE [FILE ...]]

A simple template for creating a Python CLI tool that reads 
line-delimited, CSV or JSON Lines formatted data from files 
or standard input.

positional arguments:
  FILE                  files to read, if empty, stdin is used

optional arguments:
  -h, --help            show this help message and exit
  -if INPUT_FORMAT, --input-format INPUT_FORMAT
                        Input file format [csv, json, line]
  -id DELIMITER, --input-delimiter DELIMITER
                        character used to separate csv fields
  -o [OUTPUT_FILENAME], --output-filename [OUTPUT_FILENAME]
                        Name of output file
  -v, --verbose         Print Logging Level INFO or higher
  -d, --debug           Print Logging Level DEBUG or higher
  --version             show program's version number and exit

Usage:
    $ ./cli.py file1.txt
    $ ./cli.py file2.csv --input-format csv
    $ ./cli.py file2.csv --input-format --input-delimiter="|"
    $ ./cli.py file3.jsonl --input-format json
    $ cat file1.csv | ./cli.py --input-format csv
    $ ./cli.py file1.txt --output-filename file1.csv
```
