import Document
import DocumentToken
import Index
import Query
import Print
import IDF
import Ranking
import os


path = 'DocumentCollection'
documentTermDict = DocumentToken.documentstokens(path)
positionalIndexDict, documentFrequency = Index.postionalIndex(documentTermDict)
tf_matrix, documents, terms, = IDF.counterVictorize(documentTermDict)
tf_w_matrix = IDF.computeTf_w_matrix(tf_matrix)
idf = IDF.computeIDF(tf_w_matrix, len(documents), terms)
tf_idf = IDF.computeTF_IDF(tf_w_matrix, idf)
documentLengthDict = IDF.computeDocumentsLength(tf_idf, documents)
normalizedTF_IDF = IDF.computeNormalizedTF_IDF(tf_idf, documentLengthDict)

while(True):
    print('To print positional index please enter 1')
    print('To write phrase query please enter 2')
    print('To print Term Frequency(TF) matrix please enter 3')
    print('To print Term Frequency wtf(1 + log) matrix please enter 4')
    print('To print IDF matrix please enter 5')
    print('To print TF-IDF matrix please enter 6')
    print('To print documents length matrix please enter 7')
    print('To print normalized TF-IDF matrix please enter 8')
    print('To write phrase query and retreive document ranked with cosine similarity please enter 9\n')
    choice = input('please enter your choice: ')
    if not choice.isdecimal():
        print('please enter valid number')

    else:
        choice = int(choice)
        match choice:
            case 1:
                Print.printPostionalIndex(positionalIndexDict, documentFrequency)

            case 2:
                print('instructions for phrase query')
                print('you must write phrase query with space between each term')
                print('Notes')
                print('optionally you can write an proximity query like this: term /number term')
                print('in the proximity query, you can’t use / only or followed by characters ')
                print('it must be / followed with a number followed with space \n')
                phrase = input('please enter your phrase query as we mentioned before: ')
                matchedDocument = Query.phraseQuery(positionalIndexDict, phrase)
                if matchedDocument == -1:
                    print('invalid proximity Query\n')

                elif matchedDocument == 404:
                    print('No document have matched with query\n')
                else:
                    print('matched document is : ' + Print.listToString(matchedDocument))
                    flag = input('are you want to see document content?\n for Yes enter (Y/y) for No enter any anthor chracter : ')
                    if(flag == 'y' or flag == 'Y'):
                        for document in matchedDocument:
                            print(document + ' : ' + Document.ReadDocument(os.path.join(path, document)))

            case 3:
                print('%70s' %"Term Frequency(TF)")
                Print.printMatrixWithInt(tf_matrix, documents, terms)

            case 4:
                print('%70s' % "Term Frequency wtf(1 + log)")
                Print.printMatrixWithFloat(tf_w_matrix, documents, terms)

            case 5:
                Print.printIDF(idf)

            case 6:
                print('%70s' % "TF-IDF")
                Print.printMatrixWithFloat(tf_idf, documents, terms)

            case 7:
                print('%50s' % "Documents Length")
                Print.printDocumentsLength(documentLengthDict)

            case 8:
                print('%70s' % "normalized TF-IDF")
                Print.printMatrixWithFloat(normalizedTF_IDF, documents, terms)

            case 9:
                phrase = input('please enter your query: ')
                query, _ = Query.extractQuery(phrase)
                query = Ranking.filterOfUnknownWords(terms, query)
                if (len(query) != 0):
                    queryTF_raw = IDF.queryToVector(query, terms)
                    queryTF_w = IDF.computeTf_w_matrix([queryTF_raw])
                    queryTF_IDF = IDF.computeTF_IDF(queryTF_w, idf)
                    queryLength = IDF.computeDocumentsLength(queryTF_IDF, ["query"])
                    queryNormalizedTF_IDF = IDF.computeNormalizedTF_IDF(queryTF_IDF,queryLength)
                    collectionSimilarityWithQuery, rankedListOfCollection =\
                        Ranking.RankCollectionWithQuery(queryNormalizedTF_IDF, normalizedTF_IDF)

                    Print.printQueryProcessing(queryTF_raw, queryTF_w[0], idf, queryTF_IDF[0], queryNormalizedTF_IDF, terms)
                    print("\nquery Legnth = " + str(queryLength.get("query")) + '\n')
                    Print.printMatrixWithFloat(collectionSimilarityWithQuery, documents, terms)
                    Print.printSum(rankedListOfCollection)
                    sortedIndex = sorted(range(len(rankedListOfCollection)), key=lambda k: rankedListOfCollection[k],reverse=True)
                    mostThreeReleventsdocuments = [documents[index] for index in sortedIndex[:3]]
                    print("\nthe most three relevant document is ", Print.listToString(mostThreeReleventsdocuments))
                    flag = input('are you want to see document content?\n for Yes enter (Y/y) for No enter any anthor chracter : ')
                    if (flag == 'y' or flag == 'Y'):
                        for document in mostThreeReleventsdocuments:
                            print(document + ' : ' + Document.ReadDocument(os.path.join(path, document)))
                else:
                    print('\nNo document have matched with query\n')
            case _:
                print('invalid choice')

    again = input('\nare you want to do another operation?\n for Yes enter (Y/y) for No enter any anthor chracter : ')
    if(again != 'y' and again != 'Y'):
        break
print('\n\nThank you for using our Information Retrieval System ^_^')