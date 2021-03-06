# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 16:25:27 2017

@author: Raghav
"""

import numpy as np   
import matplotlib.pyplot as plt 
import pandas as pd 

#Importing Dataset
dataset = pd.read_csv('Advertising.csv')
X = dataset.iloc[:, 1:-1].values   # Matrix of features X
y = dataset.iloc[:, 4].values     # vector of labels 


#Splitting the dataset into the training and test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state= 42)

#Theta_best calculations using normal Equation
X_train_b = np.c_[np.ones((160,1)), X_train] # Adding x0=1 to each instance
theta_best = np.linalg.inv(X_train_b.T.dot(X_train_b)).dot(X_train_b.T).dot(y_train)
X_test_b = np.c_[np.ones((40,1)), X_test] # Adding x0=1 to each instance
y_predict= X_test_b.dot(theta_best)  #predicting the test set
y_predict_train= X_train_b.dot(theta_best)  #predicting the train set

#Cost function or Mean Square Error calclations
from sklearn.metrics import mean_squared_error
mse= mean_squared_error(y_test, y_predict)


#Fitting simple linear regression to the Training Set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)
regressor.intercept_ , regressor.coef_

#Predicting the Test set Results
y_pred = regressor.predict(X_test)


#Correleation matrix
corr_matrix = dataset.corr()


# Scatter matrix
from pandas.tools.plotting import scatter_matrix
attributes = ["TV", "radio","newspaper","sales"]
scatter_matrix(dataset[attributes], figsize=[12,8])

#Visualizing the Training set results
plt.scatter(X_train, y_train, color= 'red')
plt.plot(X_train, regressor.predict(X_train), color= 'blue')
plt.title('Sales vs Advertsising budget for TV (Training set)')
plt.xlabel('Advertising budget for TV')
plt.ylabel('Sales')
plt.show()


#Visualizing the Testing set results
plt.scatter(X_test, y_test, color= 'red')
plt.plot(X_train, regressor.predict(X_train), color= 'blue')
plt.title('Sales vs Advertsising budget for TV (Training set)')
plt.xlabel('Advertising budget for TV')
plt.ylabel('Sales')
plt.show()
