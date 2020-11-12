# -*- coding: utf-8 -*-
"""
Created on Sat May 16 18:44:35 2020

@author: TARUN

"""
import os
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split 
from sklearn import metrics

targetdir="data/processed_final_data/"
filelist = os.listdir(targetdir)

df_list = [pd.read_csv(targetdir+file) for file in filelist] 
data = pd.concat(df_list)

features=['seconds','x','y','z','heartrate']
X = data[features]
y = data['sleep_stage']

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


knn_clf = KNeighborsClassifier()

knn_clf = knn_clf.fit(X_train,y_train)

y_pred = knn_clf.predict(X_test)

print("Accuracy of KNN Classifier:",metrics.accuracy_score(y_test, y_pred))





