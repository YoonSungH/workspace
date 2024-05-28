import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

figure = plt.figure()
data = pd.read_csv('Fish.csv')

bream_length = data.loc[data.Species == 'Bream', ['Length2']].iloc[:,0].to_list()

bream_weight = data.loc[data.Species == 'Bream', ['Weight']].iloc[:,0].to_list()

smelt_length = data.loc[data.Species == 'Smelt', ['Length2']].iloc[:,0].to_list()

smelt_weight = data.loc[data.Species == 'Smelt', ['Weight']].iloc[:,0].to_list()

# 머신러닝 알고리즘은 크게 지도학습과 비지도학습으로 나뉜다.
# 비지도학습(Unsupervised Learning) 타깃 없이 입력 데이터만 사용













# 그래프를 겹칠 경우
# plt.scatter(bream_length, bream_weight)
# plt.scatter(smelt_length, smelt_weight)
# plt.title('Bream & Smelt')
# plt.xlabel('length')
# plt.ylabel('weight')



### Test set 작성
fish_length = bream_length +smelt_length
fish_weight = bream_weight +smelt_weight
# print(len(fish_length),len(fish_weight))
fish_data = [[l,w] for l,w in zip(fish_length,fish_weight)]
fish_target = [1]*35 + [0]*14

# print(fish_data[0:5]) # 리스트의 슬라이싱에서 마지막 인덱스는 포함하지 않는다.

# 1. Sampling bios(샘플링 편향) 적인 Train set 작성
train_input = fish_data[:35]
train_target = fish_target[:35]

test_input = fish_data[35:]
test_target = fish_target[35:]
kn = KNeighborsClassifier()
kn.fit(train_input,train_target)
score = kn.score(test_input,test_target)
print(score) # 0.0 출력 됨 ==> 훈련세트와 테스트세트의 편향적인 구성으로 정확도가 매우 나쁨

# 2. Sampling unbios(샘플링 비편향) 적인 Train set 작성
np_fish_data = np.array(fish_data) # fish_data 를 numpy로 변형
np_fish_target = np.array(fish_target) # fish_target 을 numpy로 변형
# print(np_fish_data);print(np_fish_data.shape)

np.random.seed(42)
index = np.arange(49)
np.random.shuffle(index) # 섞기
print(index)
# print(np_fish_data[[1,3]]) # 넘파이는 슬라이싱 외에 배열 인덱싱기능 제공(복수개의 데이터를 개별 선택)

train_input = np_fish_data[:35]
train_target = np_fish_target[:35]
print(train_input)

print(np_fish_data[13],train_input[0])

test_input = np_fish_data[index[35:]]
test_target = np_fish_target[index[35:]]

# plt.figure(1)
# train_input_length = [x[0] for x in train_input]
# train_input_weight = [x[1] for x in train_input]
#
# test_input_length = [x[0] for x in test_input]
# test_input_weight = [x[1] for x in test_input]
# plt.scatter(train_input_length, train_input_weight, c=train_target)
# plt.scatter(test_input_length, test_input_weight,c=test_target,cmap='bwr')
# plt.xlabel('Length')
# plt.ylabel('Weight')
# plt.colorbar(label='Target')
#
# plt.show()

kn.fit(train_input,train_target)
print(kn.score(test_input,test_target))
print(kn.predict(test_input))
print(test_target)
print(test_input)
print(kn.predict([[25,150]]))

# print(fish_data)
#
# fish_target = [1]*35 + [0]*14
# print(fish_target)
#
# from sklearn.neighbors import KNeighborsClassifier
#
# kn = KNeighborsClassifier()
# kn.fit(fish_data,fish_target) # 학습
#
# score = kn.score(fish_data,fish_target) # 정확도
# print("정확도 %.1f" %(score))
#
# w = 600; l= 30
# print(kn.predict([[l,w]]))
# print(kn._fit_X)
#
#
# plt.scatter(l,w,marker="^",color="r")
# plt.show()
#
# kn49= KNeighborsClassifier(n_neighbors=49)
# kn49.fit(fish_data,fish_target)
# score2 =kn49.score(fish_data,fish_target)
# print("정확도 : %.1f " % (score2))
