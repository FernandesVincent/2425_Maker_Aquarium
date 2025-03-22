import cv2

def pixel_value(frame, X, Y):
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
    pixel_val = hsv_frame[Y, X]
    return pixel_val
