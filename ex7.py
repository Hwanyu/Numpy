import numpy as np
import matplotlib.pyplot as plt 

imsi6 = np.zeros((200,200))
x = np.arange(200)
y = np.arange(200)
X,Y = np.meshgrid(x,y)
a = np.array([0,120])
b = np.array([140,0])
c = np.array([150,199])
inc1 = (b[1]-a[1])/(b[0]-a[0]) 
inc2 = (c[1]-a[1])/(c[0]-a[0]) 
inc3 = (c[1]-b[1])/(c[0]-b[0]) 
for i in range(0,200):
  for j in range(0,200):
    str1 = (inc1*(x[i]-a[0])) - (y[j]-a[1]) 
    str2 = (inc2*(x[i]-a[0])) - (y[j]-a[1]) 
    str3 = (inc3*(x[i]-b[0])) - (y[j]-b[1]) 
    if (str1<0 and str2>0 and str3<0):
      imsi6[i,j] = 1 
    else:
      imsi6[i,j] = 0 
plt.imshow(imsi6,'gray')
plt.show()
