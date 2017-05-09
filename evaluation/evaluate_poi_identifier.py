#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 


features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.3, random_state=42)


clf = DecisionTreeClassifier()
clf.fit(features_train,labels_train)

pred = clf.predict(features_test)

print clf.score(features_test,labels_test)
num_pois = sum(i == 1. for i in labels_test)
print "POIs in data set", num_pois
num_peoples = len(labels_test)
print "peoples in data set", num_peoples
print (num_peoples-4)/float(num_peoples)


#pred =          [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
#labels_test =   [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]


print confusion_matrix(labels_test,pred)
print "precision score", precision_score(labels_test, pred), "recall score", recall_score(labels_test,pred), "f1 score", f1_score(labels_test,pred)
