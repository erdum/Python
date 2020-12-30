import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.metrics import r2_score

data = pd.read_csv("http://erdum.42web.io/index.csv")

# Slicing data sets for training
train = data[:int((len(data)*0.8))]
test = data[int((len(data)*0.8)):]

# Creating numpy arrays for training
train_x = np.array(train[["ENGINESIZE"]])
train_y = np.array(train[["CO2EMISSIONS"]])

# Creating numpy arrays for testing
test_x = np.array(test[["ENGINESIZE"]])
test_y = np.array(test[["CO2EMISSIONS"]])

# Training model for prediction
regr = linear_model.LinearRegression()
regr.fit(train_x, train_y)

# User defined function to calculate prediction according to our linear line
def get_reg_prediction(in_features, intercept, slope):
  result = in_features*slope + intercept
  return result
  
# Printing predicted value for engine size of 3.5
prediction = get_reg_prediction(3.6, regr.intercept_[0], regr.coef_[0][0])

# Calculating accuracy of our model
accuracy = r2_score(regr.predict(test_x), test_y)
print (accuracy*100, "%")
