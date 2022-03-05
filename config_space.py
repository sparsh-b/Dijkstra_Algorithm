import cv2 
from math import sqrt
import numpy as np

clearance = 5

def rectangle(x, y): #return true if the point is inside the rectangle
    if x > 0+clearance and x < 400-clearance:
        if y > 0+clearance and y < 250-clearance:
            return True
    return False

def circle(x, y): #return true if the point is outside the circle
    if ((x-300)**2 + (y-185)**2 - (40+clearance)**2) > 0:
        return True
    return False

def hexagon(x, y): #return true if the point is outside the hexagon
    a = 80/sqrt(3)
    if  x>=160 and x<=240 and \
        y <= ((1/sqrt(3))*(x-200))+100+a and \
        y <= ((-1/sqrt(3))*(x-200))+100+a and \
        y >= ((1/sqrt(3))*(x-200))+100-a and \
        y >= ((-1/sqrt(3))*(x-200))+100-a:
        return False
    return True

def quadrilateral(x, y): #return true if the point is outside the quadrilateral
    if  (y >= ((-5/44)*(x-80)) + 180 and \
        y <= (25*x+14129.31)/79 and \
        y >= (6*x+733.9)/7) or \
        (y <= ((-5/44)*(x-80)) + 180 and \
        y >= (-85*x+15277.6)/69 and \
        y <= (-16*x+2263.82)/5):
        return False
    return True

def is_valid(x,y=-1): #Returns True if the point of interest lies within navigable space
    if isinstance(x, list):
        assert y == -1
        y = x[1]
        x = x[0]
    else:
        assert isinstance(x,int)
        assert isinstance(y,int) and y != -1
    if rectangle(x,y) and circle(x,y) and hexagon(x,y) and quadrilateral(x,y):
        return True
    return False

map_img = np.zeros((250, 400, 3)) #The obstacles are colored black & the navigable space is colored white.
for i in range(400):
    for j in range(250):
        if rectangle(i, j) and circle(i,j) and hexagon(i,j) and quadrilateral(i,j):
            map_img[j,i] = [255, 255, 255]

######## img = np.expand_dims(img, 2)
# flipped_img = np.flip(map_img, 0)
# print(map_img.shape)
# cv2.imshow('frame', flipped_img)
# cv2.imwrite('config_space.jpg', flipped_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()