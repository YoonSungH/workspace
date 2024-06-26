import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error
import numpy as np

knr = KNeighborsRegressor()
data = pd.read_csv('Fish.csv')

Perch_length = data.loc[data.Species == 'Perch', ['Length2']].iloc[:,0].to_list()
Perch_weight = data.loc[data.Species == 'Perch', ['Weight']].iloc[:,0].to_list()

train_input,test_input,train_target,test_target = (
    train_test_split(Perch_length,Perch_weight,random_state=42))

print(type(train_target),len(train_target))

train_input = np.array(train_input).reshape(-1,1) # 크기에 -1을 지정하면 나머지 원소 개수로 모두 채워라
test_input = np.array(test_input).reshape(-1,1) # 크기에 -1을 지정하면 나머지 원소 개수로 모두 채워라

train_poly = np.column_stack((train_input**2,train_input))
test_poly = np.column_stack((test_input**2,test_input))
print(train_poly.shape,test_poly.shape)

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(train_poly,train_target)
print(lr.predict([[50**2,50]]))
print(lr.coef_,lr.intercept_)

point = np.arange(15,50)
plt.scatter(train_input,train_target)
plt.plot(point,1.01*point**2 - 21.6*point + 116.05)

plt.plot([50],[1574],marker="^")
plt.xlabel('length');plt.ylabel('weight')
plt.show()
print(lr.score(train_poly,train_target))
print(lr.score(test_poly,test_target))

