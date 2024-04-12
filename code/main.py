import cv2
from util import get_limits
from PIL import Image

facecam = cv2.VideoCapture(0)
detect_color = [0,255,0]
while True:
    ret,frame = facecam.read()

    hsv_image = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    l_limit,u_limit = get_limits(color=detect_color)

    mask = cv2.inRange(hsv_image,l_limit,u_limit)
    contours, hirarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        if cv2.contourArea(c)>50:
            x,y,w,h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
    #new_mask = Image.fromarray(mask)
    #bounding_box = new_mask.getbbox()

    #if bounding_box is not None:
     #   x1,y1,x2,y2 = bounding_box
      #  frame = cv2.rectangle(frame,(x1,y1),(x2,y2),(0,0,255),2)


    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

facecam.release()
cv2.destroyAllWindows()