#model for predicting the avrage temprature of every month,annual,
# the three diffrence secions in india.
#the temprature is in degree celcius
#the predicted tempratue is based on the Avrage tempratue of1900-2017

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

#getting the datafrom source 

data=pd.read_csv("temp.csv")
print(data)

#Faature Extrection
ye=data[['YEAR']]
an=data[['ANNUAL']]

#graph between Avrage temprature and year
plt.title("incresing the temprature in every year")
plt.xlabel(" years ")
plt.ylabel("Avrage Annual temprature in degree celcius")
plt.plot(ye,an)
plt.show()

#traninig the given data
x_train,x_test,y_train,y_test=train_test_split(ye,an,test_size=0.2,random_state=42)

model=LinearRegression()
model.fit(x_train,y_train)



#Giving the inputs and getting the output from the model

year=int(input("enter the year"))

pred=model.predict([[year]])
print(f"the avg tempratuere will be :{pred}")

if pred[0]>100:
    print("The earth will be in Danger ")
else:
    print("The earth is not in danger")


