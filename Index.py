positionalIndexDict = dict()
documentFrequency = dict()



def postionalIndex(documetTermDictionary):
    documentsNames = documetTermDictionary.keys()
    for documentName in documentsNames:
        addTermsToDict(documentName, documetTermDictionary[documentName])
    return positionalIndexDict, documentFrequency



def addTermsToDict(documentName, termsList):
    global positionalIndexDict
    global documentFrequency
    for index, term in enumerate(termsList):
        if positionalIndexDict.get(term) == None:
            documentFrequency[term] = 1
            positionalIndexDict[term] = {documentName: [index + 1]}
        elif positionalIndexDict[term].get(documentName) == None:
            positionalIndexDict[term][documentName] = [index + 1]
            documentFrequency[term] += 1
        else:
            positionalIndexDict[term][documentName].append(index + 1)
            documentFrequency[term] += 1

