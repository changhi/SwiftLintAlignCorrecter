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
        with open(filePath) as fileToCorrect:
            for num, line in enumerate(fileToCorrect):
                if i == 
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
    newFile = newFile.split(".")
    newName = os.path.dirname(orignalFile) + "/" + newFile[0] + "_copy." + newFile[1]
    return newName


def main():
    try:
        warnFilePath = sys.argv[1]
        correctAlignment(warnFilePath)
    except Exception as e:
            print(str(e) + " in main()")
    print("\n******* reached end **********")


if __name__ == '__main__':
    main()
