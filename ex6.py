import numpy as np
import matplotlib.pyplot as plt 
imsi5 = np.zeros((200,200))
x = np.arange(200)
y = np.arange(200)
X,Y = np.meshgrid(x,y)
circle = (X-100)**2+(Y-100)**2 
where = np.where(circle>10000,0,1) 
imsi5 = where plt.imshow(imsi5,'gray')
plt.show()
