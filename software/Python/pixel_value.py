import cv2
import numpy as np
def pixel_value(frame, X, Y):
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
    pixel_val = hsv_frame[Y, X]
    return pixel_val

def closest_hsv_color(hsv_value, reference_colors):
    #"""Trouve la couleur HSV la plus proche en utilisant la distance euclidienne."""
    distances = [np.linalg.norm(hsv_value - ref) for ref in reference_colors]
    return reference_colors[np.argmin(distances)]