import parsing
#import read_index
#import sys
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem.lancaster import LancasterStemmer

lancaster = LancasterStemmer()

termIndex, termInfo, docIndex = parsing.Tokens()

queries = []
splitQueries = []

file = open('query_list.txt', 'r')
fileLines = file.readlines()

for line in fileLines:
    line = line.strip()
    queries.append(line)

for query in queries:
    query = query.replace('.', '')
    query = query.replace('"', '')
    query = query.replace(',', '')
    query = query.split()

    for i in range(len(query)):
        query[i] = lancaster.stem(query[i])

    splitQueries.append(query)

for query in splitQueries:
    queryNum = query[0]

    for word in query[1:]:
        print(word)
        if(termInfo.get(word) != None):
            print('Number of documents containing term: ', termInfo.get(word).get('numDocs'))
            print('\n')

#if (len(sys.argv) == 3):
#    queryFile = sys.argv[1]
#    resultsFile = sys.argv[2]



# def tfidf(docs, query):
#     vectorizer = TfidfVectorizer()
#     docTransform = vectorizer.fit_transform(docs)
#
#     query_tfids = vectorizer.transform([query])
#     cosineSimilarity = cosine_similarity(query_tfids, docTransform).flatten()
#
#     return cosineSimilarity

#def file_len(file)
#	with open(file) as f: 
#		for i,l in enumerate(f);
#			pass
#	return i + 1




    
    

    #f = open("output.txt", "a")
    #f.write(docIndex.get(" Q0 " + input1).get('docID))
   #f.write(cosineSimila
    
