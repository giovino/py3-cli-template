#!/usr/bin/env python3

import argparse
from argparse import RawTextHelpFormatter
import fileinput
import logging
import sys
import json
import csv

VERSION = '0.0.4'


def read_json(files):
    """
    Parses files formatted as JSON Lines

    :param files: List of files
    :return: List of dictionaries
    """

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
    """
    Parses files formatted as CSV

    :param files: List of files
    :param delimiter: Single character (eg. "," or ";" or "|")
    :return: List of lists
    """

    records = []

    try:
        csvreader_obj = csv.reader(fileinput.input(files), delimiter=delimiter)
    except FileNotFoundError as e:
        logging.warning(e)
        sys.exit(1)

    for r in csvreader_obj:
        records.append(r)

    return records

def read_newline(files):
    """
    Parses files formatted as line delimited

    :param files: List of files
    :return: List of strings
    """

    records = []

    try:
        for line in fileinput.input(files):
            records.append(line.rstrip())
    except FileNotFoundError as e:
        logging.warning(e)
        sys.exit(1)

    return records


def main():

    description = 'A simple template for creating a Python CLI tool that reads \n' \
                  'line-delimited, CSV or JSON Lines formatted data from files \n' \
                  'or standard input.'
    epilog_text = '''Usage:
    $ ./cli.py file1.txt
    $ ./cli.py file2.csv --csv
    $ ./cli.py file2.csv --csv --delimiter="|"
    $ ./cli.py file3.jsonl --json
    $ cat file1.csv | ./cli.py --csv
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
        "--csv",
        help="read CSV formatted file",
        dest="csv_format", action="store_true",
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
        "-o", "--output-filename",
        help="Name of output file",
        action="store", nargs="?",
        dest="output_filename", default=None,
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

    if args.output_filename is None:
       args.output_filename = args.files[0]

    if args.json_format:
        records = read_json(args.files)
    elif args.csv_format:
        records = read_csv(args.files, args.delimiter)
    else:
        records = read_newline(args.files)

    for record in records:
        print(record)

    sys.exit(0)


if __name__ == "__main__":
    main()
