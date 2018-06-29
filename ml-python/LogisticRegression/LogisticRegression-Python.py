import pandas as pd
import sklearn
from   sklearn.model_selection import train_test_split
import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.metrics import classification_report

allFeaturesNewPdDF = pd.read_csv("dat.prep.csv")
allFeaturesNewPdDF.head(5)

x_columns_list = ["V{}".format(i) for i in range(2,6)]
y_columns_list = "Y"
#Split into testing and training set
x_train, x_test, y_train, y_test = train_test_split(allFeaturesNewPdDF[x_columns_list], 
                                                        allFeaturesNewPdDF[y_columns_list], 
                                                        test_size=0.25, 
                                                        random_state=0)

x_train = allFeaturesNewPdDF[x_columns_list]
y_train = allFeaturesNewPdDF[y_columns_list]
x_test  = allFeaturesNewPdDF[x_columns_list]
y_test  = allFeaturesNewPdDF[y_columns_list]

 # all parameters not specified are set to their defaults
logisticRegr = LogisticRegression(C=1e10, fit_intercept=True)
    
#Fit
logisticRegr.fit(x_train, y_train.values.reshape((len(y_train.values,))))

# Use score method to get accuracy of model
score = logisticRegr.score(x_test, y_test)
#print("Accuracy of the Model: %s" % str(score))

#AUC - Area under the curve
roc=roc_auc_score(y_test, logisticRegr.predict_proba(x_test)[:,1])
#print("AUC of the Model     : %s" % str(roc))

#Predicted probabilities - these should sum to one.
#First column is is for 0, ie "no reply". And Second is 1 ie "reply"
predictedProbs = logisticRegr.predict_proba(x_test)
#print("Pred Probabilties    :")
#print(predictedProbs[0:2,])

#Just a check
assert  np.logical_not(np.any(predictedProbs.sum(axis=1) != 1.0)), "Probailities do not sum to 1"

#Coefficient/sensitivities of different columns
coeffs = pd.DataFrame({"columns": x_columns_list, "coeff": np.round(logisticRegr.coef_, 3).tolist()[0]})


#, "intercept":logisticRegr.intercept_[0]
{'accuracy':score, "auc":roc, "coeffs":coeffs, "predictedProbs":predictedProbs
,'logisticRegr.intercept_': logisticRegr.intercept_
}


#Also using Stats Models
import statsmodels.api as sm

X = x_train
X = sm.add_constant(X)
Y = y_train

logit_model = sm.Logit(Y,X)
result      = logit_model.fit()
print(result.summary())
#result.params

