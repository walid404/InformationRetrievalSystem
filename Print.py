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
        print('%50s: %-5d %-10f' % (term, termIDFDict.get(term)[0], termIDFDict.get(term)[1]))



def printDocumentsLength(documentLengthDict):
    for term in documentLengthDict.keys():
        print('%50s: %-10f' % (term + ' length', documentLengthDict.get(term)))


def printQueryProcessing(tf_raw, tf_w, idf, TF_IDF, normalizedTF_IDF, raws, indexList):
    print("%20s %10s %15s %10s %10s %10s" %("term", "TF_raw", "w tf(1+log tf)", "idf", "tf*idf", "normalized"))
    for index in indexList:
        print("%20s %10d %15f %10f %10f %10f" % (raws[index], tf_raw[index], tf_w[index], idf.get(raws[index])[1],
                                                 TF_IDF[index], normalizedTF_IDF[index]))


def printSum(rankingList, rowIndex):
    print('%-15s' %"sum", end='')
    for index in rowIndex:
        print('%-10f' %rankingList[index], end='')