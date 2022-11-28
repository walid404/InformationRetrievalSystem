import Tokenizer
import Document


def documentstokens(path):
    documentContent = Document.ReadDocumentCollection(path)
    documetTermDict = dict()
    collectionTokenized = Tokenizer.collectionTokenize(documentContent)
    for documentName, documentTokens in zip(Document.documentsNames, collectionTokenized):
        documetTermDict[documentName] = Tokenizer.filterStopwords(documentTokens)

    return documetTermDict