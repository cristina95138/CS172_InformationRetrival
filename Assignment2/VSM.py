import parsing
import re
import os
import heapq
#import read_index
import sys
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem.lancaster import LancasterStemmer

if (len(sys.argv) == 3):
   queryFile = sys.argv[1]
   resultsFile = sys.argv[2]

# Regular expressions to extract data from the corpus
doc_regex = re.compile("<DOC>.*?</DOC>", re.DOTALL)
docno_regex = re.compile("<DOCNO>.*?</DOCNO>")
text_regex = re.compile("<TEXT>.*?</TEXT>", re.DOTALL)

lancaster = LancasterStemmer()

termIndex, termInfo, docIndex = parsing.Tokens()

stopFile = open("stopwords.txt", "r")
stopWords = stopFile.read()
stopWords = stopWords.replace("\n", " ")
stops = []

for word in stopWords:
    stops.append(word)

def tfidf(doc, query):
    vectorizer = TfidfVectorizer(stop_words=stops)
    docTransform = vectorizer.fit_transform([doc])

    query_tfidfs = vectorizer.transform([query])
    cosineSimilarity = cosine_similarity(query_tfidfs, docTransform).flatten()

    return cosineSimilarity

queries = []
splitQueries = []
newQueries = []

file = open('query_list.txt', 'r')
fileLines = file.readlines()

for line in fileLines:
    line = line.strip()
    queries.append(line)

for query in queries:
    query = query.replace('.', '')
    query = query.replace('"', '')
    query = query.replace(',', '')
    newQueries.append(query)
    query = query.split()

    for i in range(len(query)):
        query[i] = lancaster.stem(query[i])
        query[i] = query[i].lower()

    splitQueries.append(query)

for query in newQueries:
    rankHeap = []
    allKeys = []
    splitQueryKeys = []
    splitQueryForKeys = query.split()
    for word in splitQueryForKeys[1:]:
        if termInfo.get(word) != None:
            keys = termInfo.get(word).get('postingList').keys()
            for key in keys:
                if key not in allKeys:
                    allKeys.append(key)

    queryNum = splitQueryForKeys[0]

    for doc in allKeys:
        splitString = doc.split('-', 1)
        substring = splitString[0]
        docFile = substring.lower()

        for dir_path, dir_names, file_names in os.walk("ap89_collection_small"):
            filePaths = [os.path.join(dir_path, filename).replace("\\", "/") for filename in file_names if
                        (filename != "readme" and filename != ".DS_Store" and filename == docFile)]

        filePath = filePaths[0]

        with open(filePath, 'r', encoding='ISO-8859-1') as f:
            filedata = f.read()
            result = re.findall(doc_regex, filedata)

        for document in result[0:]:
            # Retrieve contents of DOCNO tag
            docno = re.findall(docno_regex, document)[0].replace("<DOCNO>", "").replace("</DOCNO>", "").strip()

            splitQuery = query.split('  ', 1)
            substringQuery = splitQuery[1]
            fullQuery = substringQuery.lower()

            if docno == doc:
                # Retrieve contents of TEXT tag
                text = "".join(re.findall(text_regex, document)) \
                    .replace("<TEXT>", "").replace("</TEXT>", "") \
                    .replace("\n", " ")
                if not text.isspace():
                    #text = text.split(' ')
                    tfidf_val = tfidf(text, fullQuery)
                    heapq.heappush(rankHeap, (tfidf_val[0], doc))
                    heapq._heapify_max(rankHeap)

    rank = 1

    for docNum in rankHeap:
        if rank == 11:
            break
        rankInfo = heapq._heappop_max(rankHeap)
        output = str(queryNum) + ' Q0 ' + str(rankInfo[1]) + ' ' + str(rank) + ' ' + str(rankInfo[0]) + ' Exp\n'
        with open(resultsFile, 'a') as f:
            f.write(output)
        rank = rank + 1

    output = '\n'
    with open(resultsFile, 'a') as f:
        f.write(output)

f.close()

#def file_len(file)
#	with open(file) as f: 
#		for i,l in enumerate(f);
#			pass
#	return i + 1
    
