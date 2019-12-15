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
                print(line)
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
        previousLine = None
        with open(filePath) as fileToCorrect:
            for num, line in enumerate(fileToCorrect, start=1):
                if num in warningLines:
                    newLine = correctLine(previousLine, line)
                    previousLine = newLine
                    correctedCopy.write(str(newLine))
                else:
                    previousLine = line
                    correctedCopy.write(line)

        correctedCopy.close()

    except Exception as e:
        print(str(e) + "in correctFile")


def getWarning(line):
    return line.rstrip().split(": ")[1]


def getLineNumber(line):
    return int(line.split(":")[0].split("Line ")[1])


def getFileCopyPath(orignalFile):
    newFile = orignalFile.split("/")
    newFile = newFile[-1].split(".")
    newName = os.path.dirname(orignalFile) + "/" + newFile[0] + "_copy." + newFile[1]
    return newName


def correctLine(previousLine, currLine):
    if "(" in previousLine:
        print(currLine)
        numSpacesNeeded = previousLine.index("(") + 1
    else:
        numSpacesNeeded = len(previousLine) - len(previousLine.lstrip())
    print(numSpacesNeeded)
    return (" " * numSpacesNeeded) + currLine.strip(" ")


def main():
    try:
        warnFilePath = sys.argv[1]
        correctAlignment(warnFilePath)
    except Exception as e:
            print(str(e) + " in main()")
    print("\n******* reached end **********")


if __name__ == '__main__':
    main()
