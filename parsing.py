import re
import os
import zipfile
import time
import sys


# Regular expressions to extract data from the corpus
doc_regex = re.compile("<DOC>.*?</DOC>", re.DOTALL)
docno_regex = re.compile("<DOCNO>.*?</DOCNO>")
text_regex = re.compile("<TEXT>.*?</TEXT>", re.DOTALL)


with zipfile.ZipFile("ap89_collection_small.zip", 'r') as zip_ref:
    zip_ref.extractall()
   
# Retrieve the names of all files to be indexed in folder ./ap89_collection_small of the current directory
for dir_path, dir_names, file_names in os.walk("ap89_collection_small"):
    allfiles = [os.path.join(dir_path, filename).replace("\\", "/") for filename in file_names if (filename != "readme" and filename != ".DS_Store")]
    
for file in allfiles:
    with open(file, 'r', encoding='ISO-8859-1') as f:
        filedata = f.read()
        result = re.findall(doc_regex, filedata)  # Match the <DOC> tags and fetch documents

        termInfo = dict()

        for document in result[0:]:
            # Retrieve contents of DOCNO tag
            docno = re.findall(docno_regex, document)[0].replace("<DOCNO>", "").replace("</DOCNO>", "").strip()
            # Retrieve contents of TEXT tag
            text = "".join(re.findall(text_regex, document))\
                      .replace("<TEXT>", "").replace("</TEXT>", "")\
                      .replace("\n", " ")

            punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
            no_punct = ""
            for ele in text:
              if ele not in punc:
                    no_punct = no_punct + ele
            no_punct = no_punct.lower()
            text = no_punct

            stopFile = open("stopwords.txt", "r")
            stopWords = stopFile.read()
            stopWords = stopWords.replace("\n", " ")

            textList = list(text.split(' '))
            stopList = list(stopWords.split(' '))

            textList = list(filter(None, textList))
            stopList = list(filter(None, stopList))

            # https://www.geeksforgeeks.org/python-difference-two-lists/
            tokens = [i for i in textList + stopList if i not in textList or i not in stopList]

            termIndex = dict()
            docIndex = dict()

            postList = list()
            postList.append(docno)

            for token in tokens:
                inDoc = 0
                hashToken = hash(token) % ((sys.maxsize + 1) * 2)
                if token not in termInfo:
                    info = dict()
                    info['postingList'] = postList

                    termInfo[token] = info

                    termInfo[token]['numOccur'] = 0
                    termInfo[token]['numDocs'] = 0

                if token in termIndex:
                    termInfo[token]['numOccur'] = termInfo[token]['numOccur'] + 1
                else:
                    termInfo[token]['numOccur'] = termInfo[token]['numOccur'] + 1
                    termIndex[token] = hashToken
                    if inDoc < 2:
                        termInfo[token]['numDocs'] = termInfo[token]['numDocs'] + 1
                        ++inDoc

            docIndex[docno] = hash(docno) % ((sys.maxsize + 1) * 2)

            # testing code
        time.sleep(10)

        exit()