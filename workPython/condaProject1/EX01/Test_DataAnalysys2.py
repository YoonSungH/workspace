import pandas as pd

fish = pd.read_csv('https://bit.ly/fish_csv_data')

# 1번
print(pd.unique(fish['Species']))

# 2번
fish_input = fish[['Weight','Length','Diagonal','Height','Width']].to_numpy()

# 3번
fish_target = fish['Species'].to_numpy()

from sklearn.model_selection import train_test_split
train_input, test_input, train_target, test_target = (
  train_test_split(fish_input, fish_target, random_state=42))

from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
ss.fit(train_input)
train_scaled = ss.transform(train_input)
test_scaled = ss.transform(test_input)

from sklearn.linear_model import SGDClassifier
sc = SGDClassifier(loss='log_loss', max_iter=10, random_state=42) #random_state=42는 shuffle에 대한 시드값
sc.fit(train_scaled, train_target)
print(sc.score(train_scaled, train_target))
print(sc.score(test_scaled, test_target))

sc.partial_fit(train_scaled, train_target)

print(sc.score(train_scaled, train_target))
print(sc.score(test_scaled, test_target))

"""
  'log_loss' 로 loss function 을 로지스틱 손실 함수로 지정
  max_iter 값에 따라 달라질 수 있는데 훈련 반복 횟수 10으로 했을때
  작다는걸 알 수있음
  sc.partial_fit(train_scaled, train_target) 이렇게 실행하여 
  score값이 올라감
"""

import numpy as np
sc = SGDClassifier(loss='log_loss', random_state=42)
train_score = []
test_score = []
classes = np.unique(train_target)
for _ in range(0,300):
  sc.partial_fit(train_scaled, train_target, classes=classes)
  train_score.append(sc.score(train_scaled, train_target))
  test_score.append(sc.score(test_scaled, test_target))

import matplotlib.pyplot as plt
plt.plot(train_score)
plt.plot(test_score)
plt.xlabel = 'epoch'
plt.ylabel = 'accuracy'
plt.show()

sc = SGDClassifier(loss='log_loss', max_iter=100, tol=None, random_state=42)
sc.fit(train_scaled, train_target)

print(sc.score(train_scaled, train_target))
print(sc.score(test_scaled, test_target))