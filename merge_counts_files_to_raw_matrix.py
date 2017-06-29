'''
Merges featureCounts output to a single raw count matrix.
'''

import argparse
import sys


def parse_counts_file(filename, matrix=[]):
    '''
    Parses counts file into a matrix and update provided matrix.
    '''
    with open(filename, 'rU') as handle:
        handle.readline() # skips header
        handle.readline() # skips second header
        for i, line in enumerate(handle):
            arow = line.strip('\n').split('\t')
            try:
                matrix[i] = '\t'.join([matrix[i], arow[-1]])
            except IndexError:
                matrix.append('\t'.join([arow[0], arow[-1]]))
    return matrix


def print_matrix(matrix, names):
    '''
    Iterates through matrix and writes to stdout.
    '''
    sys.stdout.write('\t'.join(["Gene"] + names) + '\n')
    for line in matrix:
        sys.stdout.write(line + '\n')


def main():
    '''
    Arg parsing and central dispatch of function calls.
    '''
    # Arg parsing
    desc = "Merges featureCoutns output to a single raw count matrix."
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("counts", metavar="COUNTS", type=str, nargs="+",
                        help="featureCounts file")
    parser.add_argument("-n", "--names", metavar="NAMES", type=str, nargs="+",
                        help="names for column headers (in order)")
    args = parser.parse_args()
    # Central dispatch of function calls
    if args.names:
        names = args.names
    else:
        names = args.counts
    matrix = []
    for filename in args.counts:
        matrix = parse_counts_file(filename)
    print_matrix(matrix, names)


if __name__ == "__main__":
    main()
