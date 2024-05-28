# Cluster Algorism (군집 알고리즘 : 비지도 학습)
# 비슷한 샘플끼리만 모으기

import numpy as np
import matplotlib.pyplot as plt

fruits = np.load('fruits_300.npy')
print(fruits.shape)
print(fruits[0,0,:]) # 첫번째 이미지의 첫 행을 출력
# plt.imshow(fruits[80],cmap='gray') # 사진으로 찍은 이미지를 넘파이 배열로 변환할때 반전시킨 이미지
# plt.show()

# plt.imshow(fruits[0],cmap='gray_r')
# plt.show()

# fig,axs = plt.subplots(1,2)
# axs[0].imshow(fruits[100], cmap='gray_r')
# axs[1].imshow(fruits[200], cmap='gray_r')
# plt.show()

apple = fruits[0:100].reshape(-1,100*100)

pineApple = fruits[100:200].reshape(-1,100*100)

banana = fruits[200:300].reshape(-1,100*100)

print(apple.shape)
print(apple.mean(axis=1))

# plt.hist(np.mean(apple,axis=1),alpha=0.8)
# plt.hist(np.mean(pineApple,axis=1),alpha=0.8)
# plt.hist(np.mean(banana,axis=1),alpha=0.8)
# plt.legend(['apple','pineApple','banana'])
# plt.show()

# fig,axs = plt.subplots(1,3,figsize =(20,5) )
# axs[0].bar(range(10000),np.mean(apple,axis=0))
# axs[1].bar(range(10000),np.mean(pineApple,axis=0))
# axs[2].bar(range(10000),np.mean(banana,axis=0))
# plt.show()

apple_mean = np.mean(apple,axis=0).reshape(100,100)
pineApple_mean = np.mean(pineApple,axis=0).reshape(100,100)
banana_mean = np.mean(banana,axis=0).reshape(100,100)
#
#
# fig,axs = plt.subplots(1,3,figsize =(20,5) )
# axs[0].imshow(apple_mean,cmap='gray_r')
# axs[1].imshow(pineApple_mean,cmap='gray_r')
# axs[2].imshow(banana_mean,cmap='gray_r')
# plt.show()

abs_diff = np.abs(fruits-apple_mean)
abs_mean = np.mean(abs_diff,axis=(1,2))
apple_index = np.argsort(abs_mean)[:100]
print(abs_mean.shape)
apple,axs = plt.subplots(10,20,figsize=(10,15))
for i in range(10):
    for j in range(10):
        axs[i,j].imshow(fruits[apple_index[i*10 +j]],cmap='gray_r')
        axs[i,j].axis('off')

plt.show()