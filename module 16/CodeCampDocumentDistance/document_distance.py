'''
    Document Distance - A detailed description is given in the PDF
'''
# def freqcount(data):
#     return {i: data.count(i) for i in data}

def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    import collections
    import string
    import math
    characters = string.ascii_letters + string.digits + ' '
    dicta = ''.join(ind for ind in dict1 if ind in characters)
    dictb = ''.join(ind for ind in dict2 if ind in characters)
    dicta = ''.join(ind for ind in dicta if not ind.isdigit())
    dictb = ''.join(ind for ind in dictb if not ind.isdigit())
    dicta = dicta.lower().strip().split()
    dictb = dictb.lower().strip().split()
    newdict = load_stopwords("stopwords.txt")
    for word in list(dicta):
        if word in newdict:
            dicta.remove(word)
    for word in list(dictb):
        if word in newdict:
            dictb.remove(word)

    counter1 = collections.Counter(dicta)
    counter2 = collections.Counter(dictb)

    list1=[]
    list2=[]
    list3=[]
    for word in counter1:
        if word in counter2:
            list1.append(counter1[word]*counter2[word])
    for word in counter1:
        list2.append(counter1[word]**2)
    for word in counter2:
        list3.append(counter2[word]**2)
    nmrtr = sum(list1)
    dnmtr = math.sqrt(sum(list2)) * math.sqrt(sum(list3))
    rslt = nmrtr/dnmtr
    return rslt


    
def load_stopwords(stopwords):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords1 = []
    with open(stopwords, 'r') as words:
        for line in words:
            stopwords1.append(line.strip())
    return stopwords1

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()

    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
