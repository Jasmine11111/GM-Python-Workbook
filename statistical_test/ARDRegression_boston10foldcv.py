#+++++++++++++++++++++++++++++++++++++++++++++++++
# 10-Fold ARDRegression using Boston Dataset 
#+++++++++++++++++++++++++++++++++++++++++++++++++
#Importing sklearn, numpy pylab modules 
from sklearn.linear_model import ARDRegression
from sklearn.model_selection import cross_val_predict
from sklearn.datasets import load_boston
from sklearn.metrics import explained_variance_score, mean_squared_error
import numpy as np
import pylab as pl
#Loading boston datasets 
boston = load_boston()
# Creating Regression Design Matrix 
x = boston.data
# Creating target dataset
y = boston.target
# Create ARDRegression Regression object 
ARD= ARDRegression(alpha_1=0.01, alpha_2=0.01, lambda_1=1e-06, lambda_2=1e-06)
# Fitting a linear model using the dataset
ARD.fit(x,y)
# Y predicted values
yp = ARD.predict(x)
#Calculation 10-Fold CV
yp_cv = cross_val_predict(ARD, x, y, cv=10)
#Printing RMSE and Explained Variance
Evariance=explained_variance_score(y,yp)
Evariance_cv=explained_variance_score(y,yp_cv)
RMSE =np.sqrt(mean_squared_error(y,yp))
RMSECV=np.sqrt(mean_squared_error(y,yp_cv))
print('Method: ARDRegression Regression')
print('RMSE on the dataset: %.4f' %RMSE)
print('RMSE on 10-fold CV: %.4f' %RMSECV)
print('Explained Variance Regression Score on the dataset: %.4f' %Evariance)
print('Explained Variance Regression 10-fold CV: %.4f' %Evariance_cv)
#plotting real vs predicted data
pl.figure(1)
pl.plot(yp, y,'ro')
pl.plot(yp_cv, y,'bo', alpha=0.25, label='10-folds CV')
pl.xlabel('predicted')
pl.title('ARD Regression, alpha1,2=0.01 lambad1,2=1e-6')
pl.ylabel('real')
pl.grid(True)
pl.show()