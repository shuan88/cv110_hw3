import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("img/img1.jpg" , 0 )
print(img.shape)

img_PDF = np.zeros(255)
## PDF
for i in range(img[0]):
    for j in range(img[1]):
        
    
