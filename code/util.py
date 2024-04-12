import numpy as np
import cv2

def get_limits(color):

    col = np.uint8([[color]])
    hsv_col = cv2.cvtColor(col,cv2.COLOR_BGR2HSV)

    low_limit = hsv_col[0][0][0] - 20,100,100
    up_limit = hsv_col[0][0][0] + 20,255,255

    low_limit = np.array(low_limit,dtype=np.uint8)
    up_limit = np.array(up_limit,dtype=np.uint8)

    return low_limit,up_limit
