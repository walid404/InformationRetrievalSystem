import DocumentToken
import Print
import math


def computeIDF(termsFrequencyMatrix, numberOfDocuments, terms):
    termIDFDict = dict()
    for index, term in enumerate(terms):
        termFrequency = sum(termsFrequencyMatrix[index])
        termIDFDict[term] = [termFrequency, math.log10(numberOfDocuments/termFrequency)]

    return termIDFDict


def computeTF_IDF(termFrequencyMatrix, termIDFDict):
    for row, term in zip(range(len(termFrequencyMatrix)), termIDFDict.keys()):
        for col in range(len(termFrequencyMatrix[row])):
            termFrequencyMatrix[row][col] *= termIDFDict.get(term)[1]

    return termFrequencyMatrix



def counterVictorize(documentTermDict):
    documentsnames = list(documentTermDict.keys())
    termsNames = getTerms(documentTermDict)
    termsFrequencyMatrix = [[0 for _ in documentsnames] for _ in termsNames]
    for document in documentsnames:
        for term in documentTermDict[document]:
            termsFrequencyMatrix[termsNames.index(term)][documentsnames.index(document)] += 1

    return termsFrequencyMatrix, documentsnames, termsNames



def getTerms(documentTermDict):
    terms = set()
    for documentTerm in documentTermDict.values():
        for item in documentTerm:
            terms.add(item)
    return sorted(list(terms))


