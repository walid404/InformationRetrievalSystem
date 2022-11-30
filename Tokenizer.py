import nltk.corpus
from nltk.tokenize import word_tokenize


def collectionTokenize( documentsContant):
    collectionTokenized = []
    for document in documentsContant:
        collectionTokenized.append(word_tokenize(document))

    return collectionTokenized



def filterStopwords(documentTokens):
    stopwords = getStopWords()
    filteredDocument = []
    for word in documentTokens:
        if word not in stopwords:
            filteredDocument.append(word)

    return filteredDocument



def getStopWords():
    stopWord = set(nltk.corpus.stopwords.words('english'))
    stopWord.remove('in')
    stopWord.remove('to')
    stopWord.remove('where')
    return  stopWord


