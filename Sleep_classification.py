# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 16:46:03 2020

@author: TARUN

"""

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split 
from sklearn import metrics
import matplotlib.pyplot as plt


data=pd.read_csv('data/data_sleep.csv')
print(data.head())
data=data.mask(data==0).fillna(data.mean())

features=["Id", "HRBS", "HRD0", "HRD1", "HRD2", "HRD3", "HRD5", "HRAS", "TTB", "ST0", "ST1", "ST2", "ST3", "ST5", "TST"]
X = data[features]
y = data['SLPC']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.35, random_state=1)
dt_clf = DecisionTreeClassifier()

dt_clf = dt_clf.fit(X_train,y_train)

y_pred = dt_clf.predict(X_test)

print("Accuracy of Decision Tree Classifier:",metrics.accuracy_score(y_test, y_pred))



rf_clf = RandomForestClassifier(n_estimators=70, random_state=100)

rf_clf = rf_clf.fit(X_train,y_train)

y_pred = rf_clf.predict(X_test)

print("Accuracy of Random Forest Classifier:",metrics.accuracy_score(y_test, y_pred))


nb_clf = GaussianNB()

nb_clf = nb_clf.fit(X_train,y_train)

y_pred = nb_clf.predict(X_test)

print("Accuracy of Naive Bayes Classifier:",metrics.accuracy_score(y_test, y_pred))


knn_clf = KNeighborsClassifier(n_neighbors=10)

knn_clf = knn_clf.fit(X_train,y_train)

y_pred = knn_clf.predict(X_test)

print("Accuracy of KNN Classifier::",metrics.accuracy_score(y_test, y_pred))


de=["1360686","9961348","3509524"]
for s in de:
    data=pd.read_csv("data/processed_final_data/"+s+".txt")

    
    plt.figure(figsize=(15,10)) 
    plt.plot(data['seconds'],data['heartrate'])
    plt.xlabel('Time',fontsize=16)
    plt.ylabel('Heartrate',fontsize=16)
    plt.show()
    
    plt.figure(figsize=(15,10)) 
    plt.plot(data['seconds'],data['sleep_stage'],color='darkgoldenrod')
    plt.xlabel('Time',fontsize=16)
    plt.ylabel('Sleep stage',fontsize=16)
    plt.show()





