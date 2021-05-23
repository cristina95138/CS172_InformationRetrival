import parsing
import read_index
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

termIndex, termInfo, docIndex = parsing.Tokens()

if (len(sys.argv) == 3):
    queryFile = sys.argv[1]
    resultsFile = sys.argv[2]

def tfidf(docs, query):
    vectorizer = TfidfVectorizer()
    docTransform = vectorizer.fit_transform(docs)

    query_tfids = vectorizer.transform([query])
    cosineSimilarity = cosine_similarity(query_tfids, docTransform).flatten()

    return cosineSimilarity
     file1 = open('query_list.txt','r')

    
    f = open("output.txt", "a")
    f.write(docIndex.get(" Q0 " + input1).get('docID))
    f.write(cosineSimilarity + " Exp \n") 
    f.close()
    
