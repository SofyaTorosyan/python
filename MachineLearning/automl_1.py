# function that gets link to dataset, 
#                    the name of the target variable, 
#                    the ratios for splitting the original dataset into training and test sets. By default the values
#                    should be initialized as follows: training = 80% and test = 20%.
#                    option to specify whether the problem is regression or classification, however by default the value
#                    of this argument should be initialized to ‘auto’.
import pandas as pd
import numpy as np
from pandas import read_csv
def my_func(path, target, training_ratio = 0.8, test = 0.2, type = 'auto'):
   #load dataset
    data = pd.read_csv("train.csv")
    # classify all of the features as numeric or categorical.
    numerical_features = data.select_dtypes(include = np.number).columns
    numerical_features
    categorical_features=data.select_dtypes(include=["object"]).columns
    categorical_features
    # include = 'category' gives empty list.(?)
    # if there are missing values in the categorical features fill in them using a new category called ’other’.
    
    missing_values_count = data.isnull().sum()
    missing_values_count
    for i in range(categorical_features.size):
       for val in data[categorical_features[i]]:
          if val == np.NaN:
             val = 'other'
    # for missing values in numeric features fill in them using a new category called ’ignore’.
    for i in range(numerical_features.size):
       for val in data[numerical_features[i]]:
           if val == np.NaN:
               val = 'ignore'
            
    # If there are missing values or other categories in the test set for categorical features not included in
    # the train set you should fill in them using the same ’other’ category. 
    for i in range(categorical_features.size):
       data[categorical_features[i]] = data[categorical_features[i]].astype('category')
       data[categorical_features[i]] = data[categorical_features[i]].cat.codes
        
    # based on the target variable provided infer whether the problem is classification or regression.
    # classification? If the user does not specify
    # it and the default value ‘auto’ stays, then the program checks if the target variable is categorical or
    # numerical. If it is categorical then this is a classification task.
    check = np.array(target)
    if (check.dtype.name == 'category') | ((check.dtype.name == 'category') & (np.unique(check).size < 10)):
        type = 'classification'
    elif  np.unique(check).size == 2:
        type = 'binary_classification'
    elif  np.unique(check).size > 2:
        type = 'multiclass_classification'


