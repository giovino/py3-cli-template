# py3-cli-template
A template for creating a Python CLI tool that reads and 
writes line-delimited, CSV or JSON Lines formatted data 
to and from files or standard input 

```text
usage: cli.py [-h] [-if INPUT_FORMAT] [-id DELIMITER] [-oformat OUTPUT_FORMAT]
              [-ofile OUTPUT_FILENAME] [-v] [-d] [--version]
              [FILE [FILE ...]]

A template for creating a Python CLI tool that reads and 
writes line-delimited, CSV or JSON Lines formatted data 
to and from files or standard input

positional arguments:
  FILE                  files to read, if empty, stdin is used

optional arguments:
  -h, --help            show this help message and exit
  -if INPUT_FORMAT, --input-format INPUT_FORMAT
                        Input file format [csv, json, line]
  -id DELIMITER, --input-delimiter DELIMITER
                        character used to separate csv fields
  -oformat OUTPUT_FORMAT, --output-format OUTPUT_FORMAT
                        Output format [csv, json, line]
  -ofile OUTPUT_FILENAME, --output-filename OUTPUT_FILENAME
                        Name of output file
  -v, --verbose         Print Logging Level INFO or higher
  -d, --debug           Print Logging Level DEBUG or higher
  --version             show program's version number and exit

Usage:
    $ ./cli.py data.txt
    $ ./cli.py data.txt --input-format line
    $ ./cli.py data.csv --input-format csv
    $ ./cli.py data.csv --input-format csv --input-delimiter=","
    $ ./cli.py data.jsonl --input-format json
    $ ./cli.py data.txt --input-format line --output-format line --output-filename data1.txt
    $ ./cli.py data.csv --input-format csv --output-format csv --output-filename data1.csv
    $ ./cli.py data.jsonl --input-format json --output-format json --output-filename data1.jsonl
    $ cat file1.csv | ./cli.py --input-format csv
```
