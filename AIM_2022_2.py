#!/usr/bin/env python3

#import modules//

import cv2
import numpy
import os


#to find the green blobs later these are upper and lower
#bounds for the green blob...
lower = (0, 196, 206)
upper = (138, 255, 255)
threshold_area = 200
img_size = 224
kernel = numpy.ones((5,5),numpy.uint8)
kernel2 = numpy.ones((3,5),numpy.uint8)
weed = []


#img = cv2.imread('/home/matt/Downloads/IMG_1119.jpg')
data_path = ('/home/matt/Downloads/dandy')
li = os.listdir(data_path)


scale_percent = 10 # percent of original size
##width = int(img.shape[1] * scale_percent / 100)
##height = int(img.shape[0] * scale_percent / 100)
##dim = (width, height)
  
# resize image
for img in os.listdir(data_path):
  #  width = int(img.shape[1] * scale_percent / 100)
   # height = int(img.shape[0] * scale_percent / 100)
   # dim = (width, height)
    img = cv2.imread(os.path.join(data_path, img))
    img = cv2.resize(img,(img_size,img_size))
    mask = cv2.inRange(img, lower, upper)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel2)
    number_of_white_pix = numpy.sum(mask == 255)
    if number_of_white_pix > 369:
        weed = "dandylion"
        print (weed)
    if number_of_white_pix <= 369:
        weed = "poison ivy"
        print (weed)
        
    #print (number_of_white_pix)
    #contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    contours, hierarchy = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    #print (contours)
    #contour = max(contours, key = len)
    #contourImg = cv2.drawContours(img, contours, -1, (0,255,0), 3)
    #cv2.imshow("Contours", contourImg)
    cv2.imshow("img", img)
    cv2.imshow("mask", mask)
    #for c in contours:
        #print (len(contours))
####        if len(contours) > 0:
####            contours2 = max(contours, key = len)
####            area = cv2.contourArea(contours2)
####            print (area)
####        else:
####            contours = "0"
####            print ("none")
####    c = max(contours, key = cv2.contourArea)
####    #print (c)
####    for cnt in contours:
####        #print (cnt)
####        area = cv2.contourArea(cnt)
####        c = max(contours, key = cv2.contourArea)
####        area = cv2.contourArea(cnt)
####        #print (c)
####        print (area)
        
        #print (area)
        #if area > threshold_area:
        #    weed = "dandylion"
         #   elif:
          #      weed = "poison ivy"
##        if area < threshold_area:
##            weed = "poison ivy"
        #print (weed)
    #cv2.imshow("mask", mask)
   # cv2.imshow("image", img)
    cv2.waitKey()



















    
###img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
##
##mask = cv2.inRange(img, lower, upper)
##contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
##for cnt in contours:
##    area = cv2.contourArea(cnt)
##    if area > threshold_area:
##        weed = "dandylion"
##        print (weed)
##        
##    print (area)
###print (contours)
##blob = max(contours, key=lambda el: cv2.contourArea(el))
###print (blob)
##
##cv2.imshow("mask", mask)
##cv2.imshow("weed", img)
##cv2.waitKey()
cv2.destroyAllWindows()
