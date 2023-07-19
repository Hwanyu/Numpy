import numpy as np
import matplotlib.pyplot as plt

# 200x600 크기의 빈 행렬 생성
image = np.zeros((200, 600))

for i in range(200):
    for j in range(600):
        a = np.sqrt(((i-50)**2) + ((j-100)**2))
        b = np.sqrt(((i-50)**2) + ((j-100)**2))
        c = np.sqrt(((i-70)**2) + ((j-300)**2))
        d = np.sqrt(((i-70)**2) + ((j-300)**2))
        e = np.sqrt(((i-50)**2) + ((j-500)**2))
        f = np.sqrt(((i-50)**2) + ((j-500)**2))
        h = np.sqrt(((i-150)**2) + ((j-500)**2))
        k = np.sqrt(((i-150)**2) + ((j-500)**2))
        if (a<=25 and b >=20): #조건문 : 중간에 값 출려하기 위함
            image[i,j]=255 #중간값만 나오게 함
        elif (c<=20 and d >=15): #조건문 : 중간에 값 출려하기 위함
            image[i,j]=255 #중간값만 나오게 함
        elif (e<=25 and f >=20): #조건문 : 중간에 값 출려하기 위함
            image[i,j]=255 #중간값만 나오게 함
        elif (h<=25 and k >=20): #조건문 : 중간에 값 출려하기 위함
            image[i,j]=255 #중간값만 나오게 함


image[100:105,50:150]=255
image[100:150,80:85]=255
image[100:150,120:125]=255

image[20:25,285:315]=255
image[30:35,270:330]=255
image[100:120,298:302]=255
image[115:120,270:330]=255
image[30:120,350:355]=255
image[68:72,350:370]=255
image[130:150,310:315]=255
image[145:150,315:355]=255

image[105:110,450:550]=255
image[90:110,480:485]=255
image[90:110,515:520]=255

# 이미지 출력
plt.imshow(image, cmap='gray')
plt.axis('off')  # 축 제거
plt.show()
