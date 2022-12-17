import os


def ReadDocumentCollection(path):
    documentsContent = []
    documentsNames = FilterDocuments(os.listdir(path))
    documentsNames = SortDocuments(documentsNames)
    for documentName in documentsNames:
        documentsContent.append(ReadDocument(os.path.join(path, documentName)))

    return documentsContent, documentsNames



def FilterDocuments(documentsNames):
    filterdList = []
    for document in documentsNames:
        if document[-4:] == '.txt':
            filterdList.append(document)

    return filterdList



def ReadDocument(documentPath):
    document = open(documentPath + '.txt', 'r')
    content = document.read()
    document.close()
    return content.lower()



def SortDocuments(documentNames):
    numList = []
    strList = []
    for document in documentNames:
        document = document.replace('.txt', '')
        if document.isdecimal():
            numList.append(int(document))
        else:
            strList.append(document)
    numList = sorted(numList)
    strList = sorted(strList)
    for index in range(len(numList)):
        numList[index] = str(numList[index])
    return numList + strList



def RenameDocuments(documentsNames):
    newNames = dict()
    for index, document in enumerate(documentsNames):
        newNames['d' + str(index+1)] = document
    return newNames
