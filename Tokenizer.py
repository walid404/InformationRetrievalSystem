import Document


def collectionTokenize( documentsContant):
    collectionTokenized = []
    for document in documentsContant:
        collectionTokenized.append(Tokenize(document))

    return collectionTokenized



def filterStopwords(documentTokens):
    stopwords = getStopWords()
    filteredDocument = []
    for word in documentTokens:
        if word not in stopwords:
            filteredDocument.append(word)

    return filteredDocument



def getStopWords():
    stopword = Document.ReadDocument('English Stopwords')
    stopWord = Tokenize(stopword)
    return  stopWord

def Tokenize(document, sep=' '):
    tokens = []
    token = ''
    for index, char in enumerate(document):
        if char == sep and (index == 0 or index == len(document)-1):
            continue
        elif char == sep:
            if token != '':
                tokens.append(token)
                token = ''
        else:
            token += char
    if token != '':
        tokens.append(token)

    return tokens



