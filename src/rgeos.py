# -*- coding: utf-8 -*-
#https://github.com/rgeos/meetup/blob/master/Titanic.ipynb
#の内容を元にkaggleの形式に書き換えた。正答率は0.75ほど。

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import csv

def load_input_data(train_data_path, test_data_path):
    train = pd.read_csv('data/train.csv')
    test = pd.read_csv('data/test.csv')
    return train, test

def train_data_processing(train):
    train.drop('Cabin',axis=1,inplace=True)
    #train.dropna(inplace=True)
    train["Age"].fillna(train.Age.median(), inplace=True)
    #print(train.info())

    sex = pd.get_dummies(train['Sex'],drop_first=True)
    embark = pd.get_dummies(train['Embarked'],drop_first=True)
    train.drop(['Sex','Embarked','Name','Ticket'],axis=1,inplace=True)
    train = pd.concat([train,sex,embark],axis=1)
    X_train = train.drop('Survived',axis=1)
    y_train = train['Survived']

    return X_train, y_train

def test_data_processing(test):
    test.drop('Cabin',axis=1,inplace=True)
    test["Age"].fillna(test.Age.median(), inplace=True)
    test["Fare"].fillna(test.Age.median(), inplace=True)
    #print(train.info())
    sex2 = pd.get_dummies(test['Sex'],drop_first=True)
    embark2 = pd.get_dummies(test['Embarked'],drop_first=True)
    test.drop(['Sex','Embarked','Name','Ticket'],axis=1,inplace=True)
    X_test = pd.concat([test,sex2,embark2],axis=1)

    return X_test

def make_model(X_train, y_train):
    logmodel = LogisticRegression()
    logmodel.fit(X_train,y_train)
    return logmodel

def make_prediction(logmodel, X_test):
    predictions = logmodel.predict(X_test)
    #print(predictions)
    zip_data = zip(X_test.values[:,0].astype(int), predictions.astype(int))
    predict_data = list(zip_data)

    return predictions

def export_as_csv(file_path, test_data, output):
    with open(file_path, "w") as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(["PassengerId", "Survived"])
        for pid, survived in zip(test_data[:,0].astype(int), output.astype(int)):
            writer.writerow([pid, survived])


if __name__ == '__main__':
    #data load
    train_data, test_data = load_input_data("data/train.csv", "data/test.csv")

    #train data processing
    X_train, y_train = train_data_processing(train_data)

    #test data processing
    X_test = test_data_processing(test_data)

    #make model
    logmodel = make_model(X_train, y_train)

    #execute predictions
    predictions = make_prediction(logmodel, X_test)

    #csv export
    export_as_csv("output/rgeos_predict_result_data.csv", X_test.values, predictions)
