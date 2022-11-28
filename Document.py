import os


def ReadDocumentCollection(path):
    documentsContent = []
    global documentsNames
    documentsNames = sorted(os.listdir(path))
    for documentName in documentsNames:
        documentsContent.append(ReadDocument(os.path.join(path, documentName)))

    return documentsContent



def ReadDocument(documentPath):
    document = open(documentPath, 'r')
    content = document.read()
    document.close()
    return content