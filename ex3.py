import numpy as np
import matplotlib.pyplot as plt 
empty = np.zeros((5,5))
full = np.full((5,5),255) 
a=np.hstack((empty,full)) 
b=np.hstack((full,empty)) 
imsi1=np.vstack((a,b)) 
imsi2=np.hstack(((imsi1,imsi1))*10) 
imsi3=np.vstack((imsi2,imsi2))
for a in range(0,18):
  imsi3=np.vstack((imsi3,imsi2)) 
plt.imshow(imsi3)
plt.show()
