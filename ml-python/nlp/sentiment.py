
# coding: utf-8

# In[7]:


import nltk
import random
#-------------------------------------------------------
from nltk.classify.scikitlearn import SklearnClassifier
#-------------------------------------------------------
import pickle
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC

from nltk.classify import ClassifierI
from statistics import mode
from nltk.tokenize import word_tokenize


# In[17]:


import random

word_features_f = open("pickled_algos/word_features.pickle", "rb")
word_features = pickle.load(word_features_f)
word_features_f.close()

def find_features(document):
    words = nltk.word_tokenize(document)
    features = {}
    for w in word_features:  #note that word_features contains top 3000 words only(above)
        features[w] = (w in words)
    return(features)

class VoteClassifier(ClassifierI):
    def __init__(self, *classifiers):
        self._classifiers = classifiers
        
    def classify(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        return(mode(votes))
    
    def confidence(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
            
        choice_votes = votes.count(mode(votes))
        conf = choice_votes/len(votes)
        return conf


# In[18]:


def getClassifier(pickleFile):
    classifier_f = open(pickleFile, "rb")
    classifier_fromPickle = pickle.load(classifier_f)
    classifier_f.close()
    return(classifier_fromPickle)



voted_classfier = VoteClassifier(getClassifier("pickled_algos/MultinomialNB.pickle"),
                                 getClassifier("pickled_algos/BernoulliNB.pickle"),
                                 getClassifier("pickled_algos/LogisticRegression.pickle"),
                                 getClassifier("pickled_algos/LinearSVC.pickle"),
                                 getClassifier("pickled_algos/naivebayes.pickle"),
                                 getClassifier("pickled_algos/NuSVC.pickle"),
                                 getClassifier("pickled_algos/SGDClassifier.pickle"),
                                 getClassifier("pickled_algos/SVC.pickle"))


# In[19]:


def sentiment(text):
    features = find_features(text)
    return voted_classfier.classify(features)


# In[30]:


#sentiment("thats the best nice good thing in my life. not the worst")

