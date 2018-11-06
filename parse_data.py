def handleParsingStrings(string):
    parsedString = string.replace(",", " ")
    parsedString = parsedString.replace("[", " ")
    parsedString = parsedString.replace("]", " ")
    parsedString = parsedString.split()

    parseLength = len(parsedString)
    for i in range(parseLength):
        parsedString[i] = int(parsedString[i])

    return parsedString

def initializeTxtData():
    file = open("Asst1.data.txt", "r")
    txtDataArray = file.readlines()
    fBoundary = int(txtDataArray[0])
    fStartGoal = handleParsingStrings(txtDataArray[1])
    fStart = [fStartGoal[0], fStartGoal[1]]
    fGoal = [fStartGoal[2], fStartGoal[3]]

    fMap = txtDataArray[2:]
    length = len(fMap)
    for i in range(length):
        fMap[i] = handleParsingStrings(fMap[i])

    return {
        "boundary" : fBoundary,
        "start"    : fStart,
        "goal"     : fGoal,
        "map"      : fMap
        }
