import numpy as np
import matplotlib.pyplot as plt 
imsi4 = np.zeros((200,200)) 
imsi4[0:40,0:40]=255 
imsi4[40:80,40:80]=255 
imsi4[80:120,80:120]=255 
imsi4[120:160,120:160]=255 
imsi4[160:200,160:200]=255 
imsi5 = imsi4
plt.imshow(imsi5,'gray') 
plt.show()
