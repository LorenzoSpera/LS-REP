import numpy as np
import pandas as pd 
import sys, os
import ctypes as ct
import matplotlib.pyplot as plt

sys.path.append('/Users/lorenzospera/Desktop/read_camera.py')
#print(sys.path)
from read_camera import read

res = read()
print(res)

width  = 1536                                                        
height = 1024 


nuova = int.from_bytes(res[0], byteorder='big', signed=True)
width  = 1536
height = 1024
photo = np.zeros((height, width))
x = -1
y = -1

pixel_value = -1


for i in range(0, len(res), 2):
    x = (i / 2) % width
    y = (i / 2) / width 
    pixel_value = (int.from_bytes(res[i],byteorder='big',signed=False)+(int.from_bytes(res[i+1], byteorder='big', signed=False) <<8))
    photo[int(y)][int(x)] = pixel_value


plt.imshow(photo, origin='lower')
plt.show()

