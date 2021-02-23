from sklearn.feature_extraction.text import CountVectorizer 
from nltk.tokenize import word_tokenize  


# create a corpus of sentences  
corpus = [  "hello, how are you?",  
           "im getting bored at home. And you? What do you think?",  
          "did you know about counts",  
          "let's see if this works!",  
          "YES!!!!"  ]  

# initialize CountVectorizer with word_tokenize from nltk  
# as the tokenizer  
ctv = CountVectorizer(tokenizer=word_tokenize, token_pattern=None)  

#fit the vectorizer on corpus  
ctv.fit(corpus)  

corpus_transformed = ctv.transform(corpus)  

print(ctv.vocabulary_)


#----------------------------
# import what we need
import pandas as pd

from nltk.tokenize import word_tokenize
from sklearn import linear_model
from sklearn import metrics
from sklearn import model_selection
from sklearn.feature_extraction.text import CountVectorizer


# read the training data
df = pd.read_csv("path/IMDB Dataset.csv.zip")

# map postive to 1 and negative to 0
df.sentiment = df.sentiment.apply(lambda x: 1 if x == "positive" else 0)

# we create a new column called kfold and fill it with -1
df["kfold"] = -1

# next step is to randomize the rows of data
df = df.sample(frac=1).reset_index(drop = True)

# fetch labels
y = df.sentiment.values

# initiate the kfold class from model_selection module
kf = model_selection.StratifiedKFold(n_splits=5)

for f, (t_,v_) in enumerate(kf.split(X = df, y=y)):
    df.loc[v_, 'kfold'] = f
    
# we go over the folds created
for fold_ in range(5):
    # temporary dataframe for train and test
    train_df = df[df.kfold != fold_].reset_index(drop=True)
    test_df = df[df.kfold == fold_].reset_index(drop=True)
    
    # initialize CountVectorizer with NLTK's word_tokenize
    # function as tokenizer
    count_vec = CountVectorizer(tokenizer=word_tokenize, token_pattern=None) 
    
    # fit the vectorizer on traing data revies  
    count_vec.fit(train_df.review)
    
    # transforem traing and validation data reviews
    xtrain = count_vec.transform(train_df.review)
    xtest = count_vec.transform(test_df.review)
    
    # initialize logistic regression model
    model = linear_model.LogisticRegression()
    
    # fit the model on training data reviews and sentiment
    model.fit(xtrain, train_df.sentiment)
    
    # make predictions on test data
    # threshold for predictions is 0.5
    preds = model.predict(xtest)
    
    # calculate accuracy
    accuracy = metrics.accuracy_score(test_df.sentiment, preds)
    
    print(f"Fold: {fold_}")
    print(f"Accuracy: {accuracy}")
    print("")

The piece of code takes time to run ..

But we see 89% accuracy and all we did was use bag or words with logitic regression - amazing.

However this model took took lots of time to train, lets see we we can improve the time by using naive bayes classifier. Naive bayes classifier is quite popular in NLP tasks as the sparse matrices are huge and naive bayes is simple model. To use thi smodel, we need to change one import and the line with model. Lets see how the model performs. We will use MultinomialNB from scikit learn.


# import what we need
import pandas as pd

from nltk.tokenize import word_tokenize
from sklearn import naive_bayes
from sklearn import metrics
from sklearn import model_selection
from sklearn.feature_extraction.text import CountVectorizer


# read the training data
df = pd.read_csv("path/IMDB Dataset.csv.zip")

# map postive to 1 and negative to 0
df.sentiment = df.sentiment.apply(lambda x: 1 if x == "positive" else 0)

# we create a new column called kfold and fill it with -1
df["kfold"] = -1

# next step is to randomize the rows of data
df = df.sample(frac=1).reset_index(drop = True)

# fetch labels
y = df.sentiment.values

# initiate the kfold class from model_selection module
kf = model_selection.StratifiedKFold(n_splits=5)

for f, (t_,v_) in enumerate(kf.split(X = df, y=y)):
    df.loc[v_, 'kfold'] = f
    
# we go over the folds created
for fold_ in range(5):
    # temporary dataframe for train and test
    train_df = df[df.kfold != fold_].reset_index(drop=True)
    test_df = df[df.kfold == fold_].reset_index(drop=True)
    
    # initialize CountVectorizer with NLTK's word_tokenize
    # function as tokenizer
    count_vec = CountVectorizer(tokenizer=word_tokenize, token_pattern=None) 
    
    # fit the vectorizer on traing data revies  
    count_vec.fit(train_df.review)
    
    # transforem traing and validation data reviews
    xtrain = count_vec.transform(train_df.review)
    xtest = count_vec.transform(test_df.review)
    
    # initialize Naive Bayes model
    model = naive_bayes.MultinomialNB()
    
    # fit the model on training data reviews and sentiment
    model.fit(xtrain, train_df.sentiment)
    
    # make predictions on test data
    # threshold for predictions is 0.5
    preds = model.predict(xtest)
    
    # calculate accuracy
    accuracy = metrics.accuracy_score(test_df.sentiment, preds)
    
    print(f"Fold: {fold_}")
    print(f"Accuracy: {accuracy}")
    print("")



We See that score is low. But the Naive bayes is superfast.

Another method in nlp that most of the people these days tend to ignore or don't care to know about is called the TF-IDF. TF is the term frequencies and IDF is the inverse document frequency. It might seem difficult from these terms, but things will become apparanet with formulae TF and IDF




