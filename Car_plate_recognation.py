#the python version is 3.11.0 
# becouse of the easyocr library that i used in this project 
import cv2
from matplotlib import pyplot as plt
import numpy as np
import imutils
import easyocr  
import os
import extract_plates as ep
import easyOCR_scan as eos
IMAGE_DIR = "images"


image_paths = [
    os.path.join(IMAGE_DIR, f)
    for f in os.listdir(IMAGE_DIR)
    if f.lower().endswith(('.png', '.jpg', '.jpeg'))
]
new_plate = ep.extract_plate(image_paths[1])
print(eos.easyOCR_scan(new_plate))
