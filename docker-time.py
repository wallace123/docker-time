""" Searches docker binaries and edits the timestamp """
import os
import sys
import argparse
import re


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
    # Timestamp example: 2016-12-16T02:42:17.070078439+00:00
    regExpr = r'2016-\d\d-\d\dT\d\d:\d\d:\d\d\.\d\d\d\d\d\d\d\d\d\+\d\d:\d\d'
    searchObj = re.search(regExpr, 
                          instr,
                          re.M|re.I)

    if searchObj:
        print "timestamp found: ", searchObj.group()
    else:
        print "Timestamp not found"
        sys.exit(0)

    outstr = re.sub(regExpr,
                    r'2016-01-01T00:00:00.000000000+00:00',
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
