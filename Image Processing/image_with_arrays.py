import cv2
import numpy as np

black = np.zeros([600,600])
f_row = black[1:2,:]
f_column = black[:,1:2]

black[200:400,200:400] = 1

print(black)
cv2.imshow("Black", black)

cv2.waitKey(0)