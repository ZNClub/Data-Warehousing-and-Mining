# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 20:17:33 2017

@author: ZNevzz
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets, linear_model

def weights(X,Y):
    l = len(X)
    mean_x = sum(X)//l
    mean_y = sum(Y)//l
    
    xi=[],yi=[],xi2=[]
    for i in range(0,l):
        #temp = ((X[i]-mean_x)*(Y[i]-mean_y))/(X[i]-mean_x)**2
        temp = X[i]-mean_x
        xi.append(temp)
        yi.append(Y[i]-mean_y)
        xi2.append(temp*temp)
    
    return ((sum(xi))*(sum(yi)))/(sum(xi2))

def linear_regression(var_x,X,Y):
    ini_w = 1
    
    prediction = ini_w + weights(X,Y)*var_x
    
    return prediction



diabetes = datasets.load_diabetes()

diabetes_X = diabetes.data[:, np.newaxis, 2]

print(len(diabetes_X),len(diabetes.target))

#Use only one feature
#diabetes_X = diabetes.data[:, np.newaxis, 2]

# Split the data into training/testing sets
diabetes_X_train = diabetes_X[:300]
diabetes_X_test = diabetes_X[300:]

# Split the targets into training/testing sets
diabetes_y_train = diabetes.target[:300]
diabetes_y_test = diabetes.target[300:]

## scikit Bunch to pandas Dataframe

# np.c_ is the numpy concatenate function
# which is used to concat iris['data'] and iris['target'] arrays 
# for pandas column argument: concat iris['feature_names'] list
# and string list (in this case one string); you can make this anything you'd like..  
# the original dataset would probably call this ['Species']
#data1 = pd.DataFrame(data= np.c_[diabetes['data'], diabetes['target']],
#                     columns= diabetes['feature_names'] + ['target'])
#print(data1)

print(type(diabetes_X),type(diabetes.target))

#linear_regression(9,diabetes_X.tolist(),diabetes.target.tolist())

print(sum(diabetes_X.tolist())/442)
print(sum(diabetes.target.tolist())/442)




