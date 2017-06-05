# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib
import csv

#import data
def load_train_data(file_name="data/train.csv"):
    data = pd.read_csv(file_name).replace("male",0).replace("female",1)
    data["Age"].fillna(data.Age.median(), inplace=True)
    return data

#data processing
def data_processing(df):
    df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
    df2 = df.drop(["Name", "SibSp", "Parch", "Ticket", "Fare", "Cabin", "Embarked"], axis=1)
    #print(df2.dtypes)
    train_data = df2.values
    xs = train_data[:, 2:] # Pclass以降の変数
    y  = train_data[:, 1]  # 正解データ
    return xs, y

def make_model(xs, y, model_path):
    forest = RandomForestClassifier(n_estimators = 100)
    forest = forest.fit(xs, y)
    joblib.dump(forest, model_path)
    return forest

#main function
if __name__ == '__main__':
    #data load
    df = load_train_data("data/train.csv")
    #print(df)

    #data processing
    xs, y = data_processing(df)

    #make model
    forest = make_model(xs, y, "model/forest.pkl")
