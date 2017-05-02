# coding: utf-8

import matplotlib.pyplot as plt
#%matplotlib inline
import numpy as np
import data as pd
import os
from sklearn import datasets, linear_model

print(os.getcwd())
data=pd.read_csv('ccpv.csv',encoding ="utf-8",header =0)

print(data.head())
print(data.shape)
print(data.info())
print(data.ix[:, [0,1,2,3]])
x = data.ix[:, [0,1,2,3]]
x.head()
y=data[["PE"]]
print(y.head())

print(x.head())

from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1)
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

from sklearn.linear_model import LinearRegression
linreg = LinearRegression()
linreg.fit(x_train, y_train)

print(linreg.intercept_)
print(linreg.coef_)

#模型拟合测试集
y_pred = linreg.predict(x_test)
from sklearn import metrics
# 用scikit-learn计算MSE
print("MSE:{}".format(metrics.mean_squared_error(y_test, y_pred)))
# 用scikit-learn计算RMSE
print("RMSE:{}".format(np.sqrt(metrics.mean_squared_error(y_test, y_pred))))

x = data.ix[:,[0,1,2,3]]
y = data[['PE']]
from sklearn.model_selection import cross_val_predict
predicted = cross_val_predict(linreg, x, y, cv=10)
# 用scikit-learn计算MSE
print("MSE:{}".format(metrics.mean_squared_error(y, predicted)))
# 用scikit-learn计算RMSE
print("RMSE:{}".format(np.sqrt(metrics.mean_squared_error(y, predicted))))


fig, ax = plt.subplots()
ax.scatter(y, predicted)
ax.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=4)
ax.set_xlabel('Measured')
ax.set_ylabel('Predicted')
plt.show()