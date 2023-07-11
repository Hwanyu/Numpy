import numpy as np
import matplotlib.pyplot as plt 

imsi3 = np.zeros((200,200))
for a in range(0,9):
  imsi3[10*a:(200-10*a),10*a:(200-10*a)]=a%2 
plt.imshow(imsi3,'gray')
plt.show()
