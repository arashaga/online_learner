import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets, linear_model
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import Imputer, LabelEncoder

#make this a class later-on
##TODO: 5-process data
##TODO:     5.1-preview
##TODO:     5.2-drop na or impute header.....
##TODO      5.3 modify preview data to be able to import files with a different delimiters
def import_data(file_name):
    df = pd.read_csv(file_name)
    return df

#show how many is.null is there per columm
def get_missing_values(df):
    return df.isnull.sum()

#1 for columns
def drop_missing_values(df, option=0):
    df.dropna(axis=option)

#impute the missing data
def impute_values(df):
    imr = Imputer(missing_values='NaN', strategy='mean', axis=0)
    imr = imr.fit(df)
    return imr.transform(df.values)


#pass df['label'] to the function
def encode_categorical_variable(label):
    class_le = LabelEncoder()
    return class_le.fit_transform(label.values)



