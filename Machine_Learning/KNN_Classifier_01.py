import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.metrics import classification_report
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing

raw_data = pd.read_csv("shape.csv")

""" First we have to create three different lists for each column in our data set, because our data set is in dataframe format"""

Length = list(raw_data["Length"])

Width = list(raw_data["Width"])

Label = list(raw_data["Label"])

"""Remember that a model always want data sets in numeric format so our both features Length and Width are in numeric format but our label is not in numeric format so we have to encode it first 
Encoding work like this if we have 2 categorical data like square and rectangle then after encoding it is convert into numbers like 0 for square and 1 for rectangle.
"""

encoder = preprocessing.LabelEncoder()

Label = encoder.fit_transform(Label)

"""Now you can see our Label is encoded in numeric format"""

Label

"""Now we have to split data set into training and testing parts for that we have to give 20 items to training set and remaining 5 items to test for checking our model's accuracy"""

Label_train = Label[:19]
Length_train = Length[:19]
Width_train = Width[:19]

Label_test = Label[19:]
Length_test = Length[19:]
Width_test = Width[19:]

""" But did you notice we have two columns of features Length and Width but our model can only take one list so we have to combine our both features list into one list of pairs of tuple"""

Features = list(zip(Length_train, Width_train))

Features_test = list(zip(Length_test, Width_test))

"""Now if you look at Features we have a list of tuple pairs"""

Features

"""Now we can create our model and train it
The n_neighbors argument just tell the model that we want three k neighbors
"""

model = KNeighborsClassifier(n_neighbors=3)

model.fit(Features, Label_train)

"""Now we can find accuracy of our model"""

results = model.predict(Features_test)
print(results)

"""Now above you can see our predict results now lets compare these with actual values of these, remember there are pre made methods for finding models accuracy but i just only showing u the difference and finding accuracy by hand"""

print("Actual values: ", end="")
print(results)
print("Predicted values: ", end="")
print(Label_test)

"""So you can see above 4 results are correct and 2 are incorrect so in order to find accuracy here is the math:
divide 100 by number of values 100/6=16.66
now if we use compare all these values with each other and at the end count how many were correct in our example its 4 values which are correct then multiply 16.66 with the number of correct values 16.666*4=66% here it is how you can find accuracy of any model but it is impractical.

This all in action for any model.
"""

correct_result = 0
val = 100/len(results)
for i, value in enumerate(results):
  if value == Label_test[i]:
    correct_result+=1
print(correct_result*val)
