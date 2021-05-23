import parsing
import re
import os
#import read_index
#import sys
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem.lancaster import LancasterStemmer

# Regular expressions to extract data from the corpus
doc_regex = re.compile("<DOC>.*?</DOC>", re.DOTALL)
docno_regex = re.compile("<DOCNO>.*?</DOCNO>")
text_regex = re.compile("<TEXT>.*?</TEXT>", re.DOTALL)

lancaster = LancasterStemmer()

termIndex, termInfo, docIndex = parsing.Tokens()

def tfidf(doc, query):
    vectorizer = TfidfVectorizer()
    docTransform = vectorizer.fit_transform(docs)

    query_tfids = vectorizer.transform([query])
    cosineSimilarity = cosine_similarity(query_tfids, docTransform).flatten()

    return cosineSimilarity

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

    print(queryNum, '\n')

    rankings = dict()

    for word in query[1:]:
        if termInfo.get(word) != None:
            allKeys = termInfo.get(word).get('postingList').keys()

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
            if document == doc:
                # Retrieve contents of DOCNO tag
                docno = re.findall(docno_regex, document)[0].replace("<DOCNO>", "").replace("</DOCNO>", "").strip()
                # Retrieve contents of TEXT tag
                text = "".join(re.findall(text_regex, document)) \
                    .replace("<TEXT>", "").replace("</TEXT>", "") \
                    .replace("\n", " ")

                tfidf(text, query)


#if (len(sys.argv) == 3):
#    queryFile = sys.argv[1]
#    resultsFile = sys.argv[2]

#def file_len(file)
#	with open(file) as f: 
#		for i,l in enumerate(f);
#			pass
#	return i + 1

    #f = open("output.txt", "a")
    #f.write(docIndex.get(" Q0 " + input1).get('docID))
   #f.write(cosineSimila
    
