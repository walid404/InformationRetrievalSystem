import Tokenizer
import Document


def documentstokens(path):
    documentContent, documentsNames = Document.ReadDocumentCollection(path)
    documentsNamesDict = Document.RenameDocuments(documentsNames)
    documentsNames = list(documentsNamesDict.keys())
    documetTermDict = dict()
    collectionTokenized = Tokenizer.collectionTokenize(documentContent)
    for documentName, documentTokens in zip(documentsNames, collectionTokenized):
        documetTermDict[documentName] = Tokenizer.filterStopwords(documentTokens)

    return documetTermDict, documentsNamesDict