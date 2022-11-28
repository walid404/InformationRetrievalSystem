from nltk import word_tokenize



def phraseQuery(positionalIndexDictionary, phrase):
    query, approxmate = extractQuery(phrase)

    if query != -1:
        intermidite = positionalIndexDictionary[query[0]]
        for index in range(1, len(query)-1):
            approxmateNumber = 1 if approxmate.get(index) == None else approxmate.get(index)
            intermidite = matchDocument(intermidite, positionalIndexDictionary[query[index]], approxmateNumber)
        return intermidite.keys()
    else:
        return -1



def extractQuery(phrase):
    terms = word_tokenize(phrase)
    query = []
    aproximate = dict()
    for term in terms:
        if term[0] == '/':
            if notValidApproxmate(term):
                return -1, -1
            aproximate[len(query)] = int(term[1:])
        else:
            query.append(term)

    return query, aproximate



def notValidApproxmate(string):
    if (len(string) == 1):
        return True
    elif not string[1:].isdigit():
        return True
    else:
        return False



def matchDocument(term1, term2, appromateNumber):
    matchedDocument = dict()
    documentsContainterm1 = list(term1.keys())
    documentsContainterm2 = list(term2.keys())
    i,j = 0,0
    while (i != len(documentsContainterm1) and j != len(documentsContainterm2)):
        if documentsContainterm1[i] == documentsContainterm2[j]:
            postList1 = term1[documentsContainterm1[i]]
            postList2 = term2[documentsContainterm2[j]]
            matchedDocument[documentsContainterm1[i]] = matchPostion(postList1, postList2, appromateNumber)
            i += 1
            j += 1
        elif documentsContainterm1[i] < documentsContainterm2[j]:
            i += 1
        else:
            j += 1

    return matchedDocument



def matchPostion(postList1, postList2, appromateNumber):
    k, l = 0, 0
    matchedPostion = []
    while (k != len(postList1) and l != len(postList2)):
        if postList1[k] + appromateNumber >= postList2[l]:
            matchedPostion.append(postList2[l])
            k += 1
            l += 1
        elif postList1[k] < postList2[l]:
            k += 1
        else:
            l += 1

    return matchedPostion


