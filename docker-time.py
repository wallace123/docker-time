""" Searches docker binaries and edits the timestamp """
import os
import sys
import argparse
import re
from datetime import datetime


ONE_GB = 1024*1024*1024


def readFile(infile):
    if os.stat(infile).st_size > ONE_GB:
        print "File size too big...exiting"
        sys.exit(0)
 
    with open(infile, 'r') as f:
        f_chars = f.read()
        f.close()

    return f_chars


def subTimeStamp(instr):
    # Docker timestamp example: 2016-12-16T02:42:17.070078439+00:00
    # regExpr timestamp is reduced due to python datetime module
    # only going to 6 places in the millisecond field
    regExpr = r'2016-\d\d-\d\dT\d\d:\d\d:\d\d\.\d\d\d\d\d\d'
    searchObj = re.search(regExpr, 
                          instr,
                          re.M|re.I)

    if searchObj:
        print "timestamp found: ", searchObj.group()
    else:
        print "Timestamp not found"
        sys.exit(0)

    new_timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f")

    outstr = re.sub(regExpr,
                    new_timestamp,
                    instr)

    return outstr


def writeFile(outstr, outfile):
    with open(outfile, 'w') as f:
        f.write(outstr)
        f.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile',
                        help="Input file to search for timestamp")
    parser.add_argument('outfile',
                        help="Output file with modified timestamp")
    args = parser.parse_args()

    in_chars = readFile(args.infile)
    out_chars = subTimeStamp(in_chars)    
    writeFile(out_chars, args.outfile)


if __name__ == '__main__':
    main()
