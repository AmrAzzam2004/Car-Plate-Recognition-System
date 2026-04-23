#the python version is 3.11.0 
# becouse of the easyocr library that i used in this project 
import cv2
from matplotlib import pyplot as plt
import numpy as np
import imaplib
import easyocr  
import os 
# IMAGE_DIR = "./images"
reader = easyocr.Reader(['en'])

# image_paths = [
#     os.path.join(IMAGE_DIR, f)
#     for f in os.listdir(IMAGE_DIR)
#     if f.lower().endswith(('.png', '.jpg', '.jpeg'))
# ]

# print("image found",image_paths)