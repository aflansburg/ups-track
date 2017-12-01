import argparse
from tracker import *

parser = argparse.ArgumentParser(description="Process and return status of a .txt file of UPS numbers separated by "
                                             "newlines", usage='Usage:\n\tpy main.py [infile.txt] [outfile.txt]')
parser.add_argument('infile', type=str, nargs='?',
                    help='path location of .txt file containing tracking numbers')
parser.add_argument('outfile', type=str, nargs='?',
                    help='path location to output file')

args = parser.parse_args()
if args.infile is not None and args.outfile is not None:
    data = get_statuses(args.infile)
    write_to_file(data)
    print(data)
else:
    print(parser.usage)
