#!/usr/bin/env python3

import argparse
from argparse import RawTextHelpFormatter
import fileinput
import logging
import sys
import json
import csv

VERSION = '0.0.2'


def read_json(files):

    records = []

    try:
        for line in fileinput.input(files):
            try:
                records.append(json.loads(line))
            except json.decoder.JSONDecodeError as e:
                logging.debug(e)
                pass
    except FileNotFoundError as e:
        logging.warning(e)
        sys.exit(1)

    return records


def read_csv(files, delimiter):

    try:
        records = csv.reader(fileinput.input(files), delimiter=delimiter)
    except FileNotFoundError as e:
        logging.warning(e)
        sys.exit(1)

    return records


def main():

    description = 'A simple template for creating a Python CLI tool that reads \n' \
                  'line-delimited data from files or standard input.'
    epilog_text = '''Usage:
    $ ./cli.py file1.csv
    $ ./cli.py file1.csv --delimiter="|"
    $ ./cli.py file1.csv file2.csv
    $ ./cli.py file3.jsonl --json
    $ cat file1.csv | ./cli.py 
    '''

    parser = argparse.ArgumentParser(
        description=description,
        epilog=epilog_text,
        formatter_class=RawTextHelpFormatter,
        )
    parser.add_argument(
        "files", metavar="FILE", nargs="*",
        help="files to read, if empty, stdin is used",
        )
    parser.add_argument(
        "--delimiter",
        help="character used to separate csv fields",
        dest="delimiter", default=",",
    )
    parser.add_argument(
        "--json",
        help="read JSON Lines formatted file",
        dest="json_format", action="store_true",
        )
    parser.add_argument(
        "-v", "--verbose",
        help="Print Logging Level INFO or higher",
        action="store_const", dest="loglevel", const=logging.INFO,
        )
    parser.add_argument(
        "-d", "--debug",
        help="Print Logging Level DEBUG or higher",
        action="store_const", dest="loglevel", const=logging.DEBUG,
        default=logging.WARNING,
        )
    parser.add_argument(
        "--version", action='version',
        version='%(prog)s {}'.format(VERSION),
        )
    args = parser.parse_args()
    logging.basicConfig(level=args.loglevel)

    if sys.stdin.isatty() and not args.files:
        parser.print_help()
        sys.exit(0)

    if args.json_format:
        records = read_json(args.files)
    else:
        records = read_csv(args.files, args.delimiter)

    for record in records:
        print(record)

    sys.exit(0)


if __name__ == "__main__":
    main()
