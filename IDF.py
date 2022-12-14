import math

import Ranking


def computeIDF(termsFrequencyMatrix, numberOfDocuments, terms):
    termIDFDict = dict()
    for index, term in enumerate(terms):
        documentFrequency = sum(termsFrequencyMatrix[index])
        termIDFDict[term] = [documentFrequency, math.log10(numberOfDocuments/documentFrequency)]

    return termIDFDict


def computeTF_IDF(termFrequencyMatrix, termIDFDict):
    tf_idf_matrix = [[0 for _ in range(len(rows))] for rows in termFrequencyMatrix]
    for row, term in zip(range(len(tf_idf_matrix)), termIDFDict.keys()):
        for col in range(len(tf_idf_matrix[row])):
            tf_idf_matrix[row][col] = termFrequencyMatrix[row][col] * termIDFDict.get(term)[1]

    return tf_idf_matrix


def computeDocumentsLength(tf_idf, documents):
    documentsLengthDict = dict()
    for col, document in enumerate(documents):
        sum = 0
        if len(tf_idf) > 1:
            documentVector = Ranking.extractDocumentVector(tf_idf, col)
        else:
            documentVector = tf_idf[0]
        for dimension in documentVector:
            sum = sum + dimension ** 2
        documentsLengthDict[document] = sum ** 0.5

    return documentsLengthDict



def computeNormalizedTF_IDF(tf_idf, documentsLengthDict):
    documents = list(documentsLengthDict.keys())
    if len(tf_idf) > 1:
        return [[(tf_idf[row][col])/documentsLengthDict.get(documents[col]) for col in range(len(tf_idf[0]))]
                for row in range(len(tf_idf))]
    else:
        return [tf_idf[0][col]/documentsLengthDict.get(documents[0]) for col in range(len(tf_idf[0]))]


def counterVictorize(documentTermDict):
    documentsnames = list(documentTermDict.keys())
    termsNames = getTerms(documentTermDict)
    termsFrequencyMatrix = [[0 for _ in documentsnames] for _ in termsNames]
    for document in documentsnames:
        for term in documentTermDict[document]:
            termsFrequencyMatrix[termsNames.index(term)][documentsnames.index(document)] += 1

    return termsFrequencyMatrix, documentsnames, termsNames



def computeTf_w_matrix(tf_matrix):
    tf_w_matrix = [[0 for _ in range(len(rows))] for rows in tf_matrix]
    for row in range(len(tf_matrix)):
        for col in range(len(tf_matrix[0])):
            if tf_matrix[row][col] == 0:
                tf_w_matrix[row][col] = 0
            else:
                tf_w_matrix[row][col] = 1 + math.log10(tf_matrix[row][col])

    return tf_w_matrix



def getTerms(documentTermDict):
    terms = []
    for documentTerm in documentTermDict.values():
        for item in documentTerm:
            if item not in terms:
                terms.append(item)

    return terms


def queryToVector(query, terms):
    queryVector = [0 for _ in terms]
    for term in query:
        queryVector[terms.index(term)] += 1

    return queryVector