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

print(Perch_length);print(len(Perch_length))
print(Perch_weight);print(len(Perch_weight))

# plt.scatter(Perch_length, Perch_weight,c=Perch_weight)
# plt.title('Perch')
# plt.xlabel('length')
# plt.ylabel('weight')
# plt.colorbar(label='weight')
# plt.show()


train_input,test_input,train_target,test_target = (
    train_test_split(Perch_length,Perch_weight,random_state=42))

# test_array = np.array([1,2,3,4])
# print(test_array.shape)
# test_array = test_array.reshape(2,2)
# print(test_array.shape)

train_input = np.array(train_input).reshape(-1,1) # 크기에 -1을 지정하면 나머지 원소 개수로 모두 채워라
test_input = np.array(test_input).reshape(-1,1) # 크기에 -1을 지정하면 나머지 원소 개수로 모두 채워라
print(train_input.shape,test_input.shape)

knr.fit(train_input,train_target)
print(type(train_target),len(train_target))

# 결정계수가 정확한 숫자를 맞히는 것은 불가능, 예측하는 값이나 타깃 모두 임의의 수치이기 때문
print(knr.score(test_input,test_target)) # 테스트 셋 정확도 : 0.992809406101064
print(knr.score(train_input,train_target)) # 훈련 셋 정확도 : 0.9698823289099254
# 결론 : 훈련셋 > 테스트셋 ==> 과대 적합
# 결론 : 훈련셋 < 테스트셋 ==> 과소 적합
# 결론 ==> 농어의 훈련셋과 테스트셋은 과소적합.

test_prediction = knr.predict(test_input) # 테스트 세트에 대한 예측
print("test prediction: " , test_prediction) # 예측된 값
print("test target: " , test_target) # 예측된 값

mae = mean_absolute_error(test_target, test_prediction) # 예측된 값과 실제 값
print(mae) # 예측이 평균적으로 19g 정도 타깃과 다르다고 알 수 있음


knr.n_neighbors = 3
knr.fit(train_input,train_target)
print(knr.score(train_input,train_target))
print(knr.score(test_input,test_target))

# 최종적으로 ==>> 과대 적합일 경우 모델을 덜 복잡하게 만들어야 한다. 근접 갯수를 늘림
# 과소 적합일 경우 모델을 더 복잡하게 만들어야 한다. 근접 갯수를 줄임