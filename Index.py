positionalIndexDict = dict()
termFrequency = dict()



def postionalIndex(documetTermDictionary):
    documentsNames = documetTermDictionary.keys()
    for documentName in documentsNames:
        addTermsToDict(documentName, documetTermDictionary[documentName])
    return positionalIndexDict, termFrequency



def addTermsToDict(documentName, termsList):
    global positionalIndexDict
    global termFrequency
    for index, term in enumerate(termsList):
        if positionalIndexDict.get(term) == None:
            termFrequency[term] = 1
            positionalIndexDict[term] = {documentName: [index + 1]}
        elif positionalIndexDict[term].get(documentName) == None:
            positionalIndexDict[term][documentName] = [index + 1]
            termFrequency[term] += 1
        else:
            positionalIndexDict[term][documentName].append(index + 1)
            termFrequency[term] += 1

