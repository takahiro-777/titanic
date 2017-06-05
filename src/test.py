# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib
import csv

#import data
def load_test_data(file_name="data/test.csv"):
    data = pd.read_csv(file_name).replace("male",0).replace("female",1)
    data["Age"].fillna(data.Age.median(), inplace=True)
    data["FamilySize"] = data["SibSp"] + data["Parch"] + 1
    data2 = data.drop(["Name", "SibSp", "Parch", "Ticket", "Fare", "Cabin", "Embarked"], axis=1)
    return data2

def predict_data(model, df):
    test_data = df.values
    xs_test = test_data[:, 1:]
    output = model.predict(xs_test)
    zip_data = zip(test_data[:,0].astype(int), output.astype(int))
    predict_data = list(zip_data)
    return predict_data, test_data, output

def export_as_csv(file_path, test_data, output):
    with open(file_path, "w") as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(["PassengerId", "Survived"])
        for pid, survived in zip(test_data[:,0].astype(int), output.astype(int)):
            writer.writerow([pid, survived])

if __name__ == '__main__':
    #read model
    forest = joblib.load('model/forest.pkl')

    #load test data
    df = load_test_data("data/test.csv")

    #calculate predict data
    predict_data, test_data, output = predict_data(forest, df)
    print(predict_data)

    #export as csv-format
    export_as_csv("output/predict_result_data.csv", test_data, output)
