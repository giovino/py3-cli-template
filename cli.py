#!/usr/bin/env python3

import argparse
from argparse import RawTextHelpFormatter
import fileinput
import logging
import sys

VERSION = '0.0.1'


def main():

    description = 'A simple template for creating a Python CLI tool that reads \n' \
                  'line-delimited data from files or standard input.'
    epilog_text = '''Usage:
    $ ./cli.py file1.csv
    $ ./cli.py file1.csv file2.csv 
    $ cat file1.csv | ./cli.py
    '''

    parser = argparse.ArgumentParser(
        description=description,
        epilog=epilog_text,
        formatter_class=RawTextHelpFormatter,
    )
    parser.add_argument(
        'files', metavar='FILE', nargs='*',
        help='files to read, if empty, stdin is used',
    )
    parser.add_argument(
        "-d", "--debug",
        help="Print lots of debugging statements",
        action="store_const", dest="loglevel", const=logging.DEBUG,
        default=logging.WARNING,
    )
    parser.add_argument(
        '-v', '--verbose',
        help="Be verbose",
        action="store_const", dest="loglevel", const=logging.INFO,
    )
    parser.add_argument("--version", action='version', version='%(prog)s {}'.format(VERSION))
    args = parser.parse_args()
    logging.basicConfig(level=args.loglevel)

    records = []

    if sys.stdin.isatty() and not args.files:
        parser.print_help()
        sys.exit(0)

    try:
        for line in fileinput.input(args.files):
            records.append(line.rstrip())
    except FileNotFoundError as e:
        logging.info(e)
        sys.exit(1)

    for record in records:
        print(record)

    sys.exit(0)


if __name__ == "__main__":
    main()
