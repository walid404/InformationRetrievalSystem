import Document
import DocumentToken
import Index
import Query
import os

path = 'DocumentCollection'
documentTermDict = DocumentToken.documentstokens(path)
positionalIndexDict, termFrequency = Index.postionalIndex(documentTermDict)
while(True):
    print('To print positional index please enter 1')
    print('To write phrase query please enter 2')
    choice = int(input('please enter your choice: '))

    match choice:
        case 1:
            Index.printPostionalIndex(positionalIndexDict, termFrequency)

        case 2:
            print('instructions for phrase query')
            print('you must write phrase query with space between each term')
            print('Notes')
            print('optionally you can write an approximate query like this: term /number term')
            print('in the approximate query, you can’t use / only or followed by characters ')
            print('it must be / followed with a number followed with space ')
            phrase = input('please enter your phrase query as we mentioned before: ')
            matchedDocument = Query.phraseQuery(positionalIndexDict, phrase)
            if matchedDocument == -1:
                print('invalid approximate Query')

            elif matchedDocument == 404:
                print('No document have matched with query')
            else:
                print('matched document is : ' + Index.listToString(matchedDocument))
                flag = input('are you want to see document content? for Yes enter (Y/y) for No enter any anthor chracter : ')
                if(flag == 'y' or flag == 'Y'):
                    for document in matchedDocument:
                        print(document + ' : ' + Document.ReadDocument(os.path.join(path, document)))
        case _:
            print('invalid choice')

    again = input('are you want to do another operation? for Yes enter (Y/y) for No enter any anthor chracter : ')
    if(again != 'y' and again != 'Y'):
        break
print('Thank you for using our Information Retrieval System ^_^')