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





def printPostionalIndex(positionalIndexDict, termFrequency):
    terms = positionalIndexDict.keys()
    for term in terms:
        print('<{}, {};'.format(term, termFrequency[term]))
        documentscontainTerm = positionalIndexDict[term].keys()
        for document in documentscontainTerm:
            print('{}: {};'.format(document, listToString(positionalIndexDict[term][document])))
        print('>')


def listToString(list):
    s = ''
    for index, item in enumerate(list):
        if index != 0:
            s += ', '
        s += str(item)

    return s