""" Searches docker binaries and edits the timestamp """
import os
import sys
import argparse


ONE_GB = 1024*1024*1024


def readFile(infile):
    if os.stat(infile).st_size > ONE_GB:
        print "File size too big...exiting"
        sys.exit(0)
 
    with open(infile, 'r') as f:
        f_chars = f.read()
        f.close()

    return f_chars
        

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile',
                        help="Input file to search for timestamp")
    args = parser.parse_args()

    f_chars = readFile(args.infile)
    for i in range(10):
        print f_chars[i]


if __name__ == '__main__':
    main()
