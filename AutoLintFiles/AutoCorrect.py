import sys
import os


def safeMode():
    """Return if safeMode is enabled."""
    if sys.argv[-1] == "--safe" or sys.argv[-1] == "-s":
        return True
    return False


def correctAlignment(warnFilePath):
    try:
        warnFile = open(warnFilePath, "r")
        alignmentError = ("Function parameters should be aligned vertically " +
                          "if they're in multiple lines in a method call.")
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
        correctedCopy = []
        with open(filePath) as fileToCorrect:
            lines = fileToCorrect.readlines()
            for num, line in enumerate(lines):
                if num in warningLines:
                    newLine = correctLine(num, lines)
                    lines[num] = newLine  # override old line
                    correctedCopy.append(str(newLine))
                else:
                    correctedCopy.append(line)

            if safeMode:  # Remove original file
                os.remove(filePath)
            copyFile = open(getFilePath(filePath), "w+")
            for line in correctedCopy:
                copyFile.write(line)
            copyFile.close()

    except Exception as e:
        print(str(e) + "in correctFile")


def getWarning(line):
    return line.rstrip().split(": ")[1]


def getLineNumber(line):
    """Return line number minus 1 to account for indexing at 0."""
    return int(line.split(":")[0].split("Line ")[1]) - 1


def getFilePath(orignalFile):
    newFile = orignalFile.split("/")
    newFile = newFile[-1].split(".")
    copy = "."
    if safeMode():
        copy = "_copy."
    newName = (os.path.dirname(orignalFile) + "/" +
               newFile[0] + copy + newFile[1])
    return newName


def correctLine(current, lines):
    """Return corrected line based off current."""
    previousLine = lines[current - 1]
    if "(" in previousLine:
        numSpacesNeeded = previousLine.index("(") + 1
    else:
        numSpacesNeeded = len(previousLine) - len(previousLine.lstrip())
    return (" " * numSpacesNeeded) + lines[current].strip(" ")


def main():
    try:
        warnFilePath = sys.argv[1]
        correctAlignment(warnFilePath)

    except Exception as e:
            print(str(e))

    print("\n***** Finished Correcting Files *****\n")


if __name__ == '__main__':
    main()
