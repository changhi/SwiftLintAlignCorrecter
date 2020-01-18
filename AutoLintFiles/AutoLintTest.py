import sys


def main():
    print("in main")
    try:
        warnFile = open(sys.argv[1], "r")
        alignmentError = ("Function parameters should be aligned vertically " +
                          "if they're in multiple lines in a method call.")
        for line in warnFile.readlines():
            print(line)
            if alignmentError in line:
                print "***** Tests Failed ******"
                return 1

        warnFile.close()
    except Exception as e:
        print(str(e))


def getWarning(line):
    return line.rstrip().split(": ")[1]


if __name__ == '__main__':
    main()
