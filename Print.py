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



def printMatrixWithInt(matrix, coulmns, rows):
    print('%-15s'%"", end='')
    for coulmn in coulmns:
        print('%-10s' % coulmn ,end='')

    for index, row in enumerate(rows):
        print()
        print('%-15s' %row, end='')
        for document in matrix[index]:
            print('%-10s'%str(document),end='')

    print()



def printMatrixWithFloat(matrix, coulmns, rows):
    print('%-15s' %"", end='')
    for coulmn in coulmns:
        print('%-10s' %coulmn, end='')

    for index, row in enumerate(rows):
        print()
        print('%-15s' %row, end='')
        for document in matrix[index]:
            print('%-10f' %document, end='')
    print()

def printIDF(termIDFDict):
    print('%50s %-5s %-10s' %("term", 'df', 'IDF'))
    for term in termIDFDict.keys():
        print('%50s: %-5s %-10f' % (term, termIDFDict.get(term)[0], termIDFDict.get(term)[1]))