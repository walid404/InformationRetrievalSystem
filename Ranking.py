def cosineSimilarity(vector1, vector2):
    sum = 0
    list = []
    for x, y in zip(vector1, vector2):
        sum += x * y
        list.append(x*y)

    return sum, list



def RankCollectionWithQuery(queryVector, normalizedTF_IDF):
    detailsMatrix = []
    ranklist = []
    print(normalizedTF_IDF[0])
    for index in range(len(normalizedTF_IDF[0])):
        vector = extractDocumentVector(normalizedTF_IDF, index)
        rank, detailslist = cosineSimilarity(vector, queryVector)
        ranklist.append(rank)
        detailsMatrix.append(detailslist)

    return matrixTrasponse(detailsMatrix), ranklist


def extractDocumentVector(tf_IDF, index):
    return [tf_IDF[row][index] for row in range(len(tf_IDF))]

def matrixTrasponse(matrix):
    return [[matrix[col][row] for col in range(len(matrix))] for row in range(len(matrix[0]))]

def filterOfUnknownWords(terms,query):
    filterdQuery = []
    for term in query:
        if term in terms:
            filterdQuery.append(term)

    return filterdQuery