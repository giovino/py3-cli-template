#!/usr/bin/env python3

import argparse
from argparse import RawTextHelpFormatter
import fileinput
import logging
import sys
import json
import csv

VERSION = '0.0.5'


def read_json(files):
    """
    Parses files formatted as JSON Lines

    :param files: List of files
    :return: List of dictionaries
    """

    logging.debug("Reading JSON lines from input")

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

    logging.debug("Reading CSV from input")
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

    logging.debug("Reading line delimited from input")
    records = []

    try:
        for line in fileinput.input(files):
            records.append(line.rstrip())
    except FileNotFoundError as e:
        logging.warning(e)
        sys.exit(1)

    return records


def write_csv(records, filename=None):
    """
    Write CSV formatted data to a file or stdout.

    :param records:
    :param filename:
    :return:
    """

    if filename:
        logging.debug("Writing csv data format to a file")
        with open(filename, "w") as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerows(records)
    else:
        logging.debug("Writing csv data format to stdout")
        writer = csv.writer(sys.stdout, delimiter=',')
        for record in records:
            writer.writerow(record)
    return


def write_json(records, filename=None):
    """
    Write JSON lines formatted data to a file or stdout.

    :param records:
    :param filename:
    :return:
    """

    if filename:
        logging.debug("Writing json lines formatted data to a file")
        with open(filename, "w") as f:
            for record in records:
                print(json.dumps(record), file=f)
    else:
        logging.debug("Writing json lines formatted data to stdout")
        for record in records:
            print(json.dumps(record))
    return


def write_line(records, filename=None):
    """
    Write line delimited data to a file or stdout.

    :param records:
    :param filename:
    :return:
    """

    if filename:
        logging.debug("Writing line delimited format to a file")
        with open(filename, "w") as f:
            for record in records:
                print(record, file=f)
    else:
        logging.debug("Writing line delimited format to stdout")
        for record in records:
            print(record)
    return


def process_data(records):
    """
    Main function to process, enrich or transform data.

    :param records:
    :return:
    """

    logging.debug("Processing data")
    # Data processing logic implemented here
    for record in records:
        pass

    return records


def main():

    description = 'A template for creating a Python CLI tool that reads and \n' \
                  'writes line-delimited, CSV or JSON Lines formatted data \n' \
                  'to and from files or standard input'
    epilog_text = '''Usage:
    $ ./cli.py data.txt
    $ ./cli.py data.txt --input-format line
    $ ./cli.py data.csv --input-format csv
    $ ./cli.py data.csv --input-format csv --input-delimiter=","
    $ ./cli.py data.jsonl --input-format json
    $ ./cli.py data.txt --input-format line --output-format line --output-filename data1.txt
    $ ./cli.py data.csv --input-format csv --output-format csv --output-filename data1.csv
    $ ./cli.py data.jsonl --input-format json --output-format json --output-filename data1.jsonl
    $ cat file1.csv | ./cli.py --input-format csv
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
        "-if", "--input-format",
        help="Input file format [csv, json, line]",
        dest="input_format", action="store",
        default="line",
        )
    parser.add_argument(
        "-id", "--input-delimiter",
        help="character used to separate csv fields",
        dest="delimiter", default=",",
    )
    parser.add_argument(
        "-oformat", "--output-format",
        help="Output format [csv, json, line]",
        action="store",
        dest="output_format", default="line",
        )
    parser.add_argument(
        "-ofile", "--output-filename",
        help="Name of output file",
        action="store",
        dest="output_filename",
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

    #  Parse input files
    logging.debug("Input Format: {}".format(args.input_format))
    if args.input_format.lower() == "json":
        records = read_json(args.files)
    elif args.input_format.lower() == "csv":
        records = read_csv(args.files, args.delimiter)
    else:
        records = read_newline(args.files)

    #  Process data
    records = process_data(records)

    #  Output data
    logging.debug("Output filename: {}".format(args.output_filename))
    logging.debug("Output format: {}".format(args.output_format))
    if args.output_filename:
        if args.output_format.lower() == "csv":
            write_csv(records, args.output_filename)
        elif args.output_format.lower() == "json":
            write_json(records, args.output_filename)
        else:
            write_line(records, args.output_filename)
    else:
        if args.output_format.lower() == "csv":
            write_csv(records)
        elif args.output_format.lower() == "json":
            write_json(records)
        else:
            write_line(records)

    sys.exit(0)


if __name__ == "__main__":
    main()
