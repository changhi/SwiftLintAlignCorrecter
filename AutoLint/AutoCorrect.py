import sys
import os
from os import path


def correctAlignment(warnFilePath):
    try:
        warnFile = open(warnFilePath, "r")
        alignmentError = "Function parameters should be aligned vertically if they're in multiple lines in a method call."
        warningLines = []
        for line in reversed(warnFile.readlines()):
            if line[0] == "/":
                correctFile(line.rstrip(), warningLines)
                warningLines = []

            elif getWarning(line) == alignmentError:
                warningLines.append(getLineNumber(line))

        warnFile.close()

    except Exception as e:
        print(e)


def correctFile(filePath, warningLines):
    try:
        correctedCopy = open(getFileCopyPath(filePath), "w+")
        with open(filePath) as fileToCorrect:
            lines = fileToCorrect.readlines()
            for num, line in enumerate(lines):
                if num in warningLines:
                    newLine = correctLine(num, lines)
                    lines[num] = newLine # override old line
                    correctedCopy.write(str(newLine))
                else:
                    correctedCopy.write(line)

        correctedCopy.close()

    except Exception as e:
        print(str(e) + "in correctFile")


def getWarning(line):
    return line.rstrip().split(": ")[1]


def getLineNumber(line):
    """Return line line number minus 1 to account for indexing at 0."""
    return int(line.split(":")[0].split("Line ")[1]) - 1


def getFileCopyPath(orignalFile):
    newFile = orignalFile.split("/")
    newFile = newFile[-1].split(".")
    newName = os.path.dirname(orignalFile) + "/" + newFile[0] + "_copy." + newFile[1]
    return newName


def correctLine(current, lines):
    try:
        previousLine = lines[current - 1]
        if "(" in previousLine:
            numSpacesNeeded = previousLine.index("(") + 1
        else:
            numSpacesNeeded = len(previousLine) - len(previousLine.lstrip())
        return (" " * numSpacesNeeded) + lines[current].strip(" ")

    except Exception as e:
        print(str(e) + " in main()")

def main():
    try:
        warnFilePath = sys.argv[1]
        correctAlignment(warnFilePath)
    except Exception as e:
            print(str(e) + " in main()")
    print("\n******* reached end **********")


if __name__ == '__main__':
    main()
