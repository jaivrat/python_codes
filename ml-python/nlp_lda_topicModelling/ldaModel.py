### Taken from https://media.readthedocs.org/pdf/gensim/stable/gensim.pdf

import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',level=logging.INFO)


### From Strings to Vectors

from gensim import corpora, models, similarities

documents = ["Human machine interface for lab abc computer applications",
            "A survey of user opinion of computer system response time",
            "The EPS user interface management system",
            "System and human system engineering testing of EPS",
            "Relation of user perceived response time to error measurement",
            "The generation of random binary unordered trees",
            "The intersection graph of paths in trees",
            "Graph minors IV Widths of trees and well quasi ordering",
            "Graph minors A survey"]

print(documents)
#This is a tiny corpus of nine documents, each consisting of only a single sentence


####1. Tokenize
# remove common words and tokenize
stoplist = set('for a of the and to in'.split())
texts = [[word for word in document.lower().split() if word not in stoplist] for document in documents]

print("------------TEXTS-------------")
print(texts)


# remove words that appear only once
all_tokens = sum(texts, []) #appends
tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word) == 1)
print("-----------TOKENSONCE-------------")
print(tokens_once)


texts = [[word for word in text if word not in tokens_once] for text in texts]
print("------------TEXTS-------------")
print(texts)



#--bag of words
dictionary = corpora.Dictionary(texts)
print("-----DICTIONARY-------")
print(dictionary)

dictionary.save('/tmp/deerwester.dict')    #Store the dictionary for future reference


#To see the mapping between words and their ids:
print(dictionary.token2id)



## To actually convert tokenized documents to vectors:
new_doc = "Human computer interaction"
new_vec = dictionary.doc2bow(new_doc.lower().split())
print("----" + new_doc + "-----")
print(new_vec) # the word "interaction" does not appear in the dictionary and is ignored
#The function doc2bow() simply counts the number of occurences of each distinct word, converts the word to its  integer word id and returns the result as a sparse vector. The sparse vector [(0, 1), (1, 1)] therefore reads: in the document “Human computer interaction”, the words computer (id 0) and human (id 1) appear once; the other ten dictionary words appear (implicitly) zero times.

corpus = [dictionary.doc2bow(text) for text in texts]
corpora.MmCorpus.serialize('/tmp/deerwester.mm', corpus) # store to disk, for later use
print("----CORPUS----")
print(corpus)



###Corpus Streaming – One Document at a Time
#Note that corpus above resides fully in memory, as a plain Python list. In this simple example, it doesn’t matter much, but just to make things clear, let’s assume there are millions of documents in the corpus. Storing all of them in RAM won’t do. Instead, let’s assume the documents are stored in a file on disk, one document per line. Gensim only requires that a corpus must be able to return one document vector at a time:






