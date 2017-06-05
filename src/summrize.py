# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

#import data
def load_train_data(file_name="data/train.csv"):
    data = pd.read_csv(file_name).replace("male",0).replace("female",1)
    data["Age"].fillna(data.Age.median(), inplace=True)
    return data

#PClass
def summrize_by_PClass(split_data):
    temp = [i["Pclass"].dropna() for i in split_data]
    plt.hist(temp, histtype="barstacked", bins=3)
    plt.show()

#Age
def summrize_by_Age(split_data):
    temp = [i["Age"].dropna() for i in split_data]
    plt.hist(temp, histtype="barstacked", bins=16)
    plt.show()

#main function
if __name__ == '__main__':
    #data load
    df = load_train_data("data/train.csv")
    print(df)

    #make split_data
    split_data = []
    for survived in [0,1]:
        split_data.append(df[df.Survived==survived])

    #summrize_by_PClass(split_data)
    summrize_by_Age(split_data)
