from nltk import word_tokenize

import Tokenizer


def phraseQuery(positionalIndexDictionary, phrase):
    query, proximity = extractQuery(phrase)
    if len(query) ==0 :
        return 0
    if query != -1:
        for element in query:
            if element not in positionalIndexDictionary.keys():
                return 404

        intermidite = positionalIndexDictionary[query[0]]
        for index in range(1, len(query)):
            proximityNumber = 1 if proximity.get(index) == None else proximity.get(index)
            intermidite = matchDocument(intermidite, positionalIndexDictionary[query[index]], proximityNumber)
            if(intermidite == -1):
                return 404

        return intermidite.keys()
    else:
        return -1



def extractQuery(phrase):
    terms = word_tokenize(phrase)
    query = []
    proximity = dict()
    if notValidproximity(terms[0]) and notValidproximity(terms[-1]):
        for term in terms:
            if term[0] == '/':
                if notValidproximity(term):
                    return -1, -1
                proximity[len(query)] = int(term[1:])
            else:
                query.append(term)
        query = Tokenizer.filterStopwords(query)
        return query, proximity
    else:
        return -1, -1



def notValidproximity(string):
    if (len(string) == 1):
        return True
    elif not string[1:].isdecimal():
        return True
    else:
        return False



def matchDocument(term1, term2, proximityNumber):
    matchedDocument = dict()
    documentsContainterm1 = list(term1.keys())
    documentsContainterm2 = list(term2.keys())
    i,j = 0,0
    while (i != len(documentsContainterm1) and j != len(documentsContainterm2)):
        if documentsContainterm1[i] == documentsContainterm2[j]:
            postList1 = term1[documentsContainterm1[i]]
            postList2 = term2[documentsContainterm2[j]]
            matchedpostionsList = matchPostions(postList1, postList2, proximityNumber)
            if len(matchedpostionsList) > 0 :
                matchedDocument[documentsContainterm1[i]] = matchedpostionsList
            i += 1
            j += 1
        elif documentsContainterm1[i] < documentsContainterm2[j]:
            i += 1
        else:
            j += 1

    return matchedDocument if len(matchedDocument.keys()) > 0 else -1



def matchPostions(postList1, postList2, proximityNumber):
    k, l = 0, 0
    matchedPostion = []
    while k < len(postList1) and l < len(postList2):
        if postList1[k] + proximityNumber >= postList2[l]:
            matchedPostion.append(postList2[l])
            k += 1
            l += 1
        elif postList1[k] < postList2[l]:
            k += 1
        else:
            l += 1

    return matchedPostion


def extractMatrix(matrix, cols, rows, matchedDocument, query):
    rowIndexList = []
    for term in query:
        rowIndexList.append(rows.index(term))

    colIndexlist = []
    for document in matchedDocument:
        colIndexlist.append(cols.index(document))

    newCol = [cols[index] for index in colIndexlist]
    newRows = [rows[index] for index in rowIndexList]
    newMatrix = [[matrix[row][col] for col in colIndexlist] for row in rowIndexList ]


    return newMatrix, newCol, newRows, rowIndexList, colIndexlist


