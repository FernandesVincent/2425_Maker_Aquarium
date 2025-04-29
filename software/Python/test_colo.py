import cv2
import pixel_value
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 2560)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,1440)

liste_H = list(range(181))
liste_S = list(range(256))
liste_V = list(range(256))
while(True): 
    _, frame = cap.read()  
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
    height, width, _ = frame.shape

    centerX = int(width/2)
    centerY = int(height/2)
    cv2.circle(frame, (centerX,centerY), 5, (255, 0,0), 3)
    cv2.imshow("Frame", frame)


    #pick pixel value
    #pixel_center = hsv[centerY, centerX]
    #print(pixel_center)

    #val = pixel_value.pixel_value(frame, centerX, centerY)
    #print(val)
    #val_test = [7,81,164]
    #if np.any(val == val_test):
    #   break

    key = cv2.waitKey(1)
    if key ==27: 
        break

cap.release()
cv2.destroyAllWindows()

