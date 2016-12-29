""" Searches docker binaries and edits the timestamp """
from optparse import OptionParser

def main():
    parser = OptionParser(usage="usage %prog [options] filename")

    parser.add_option("-f", "--file",
                      action="store_true",
                      dest="docker_file",
                      default=False,
                      help="read in the docker binary file for timestamp modification")

    (options, args) = parser.parse_args()

    if len(args) != 1:
        parser.error("wrong number of arguments")


if __name__ == '__main__':
    main()
