# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 19:28:58 2023

@author: Payam_(cyrus)
"""



import numpy as np
import winsound
import math 
import pylab as plt


def grund_truths_calcuater_test(x,y,width_vehicle,height_vehicle,orientation_vehicle):
    
        # 0	30	1319	2338	35	11	56.4516
        # 0	20	4405	2262	83	27	139.376
        
# x=1319
# y=2338
# width_vehicle=35
# height_vehicle=11
# orientation_vehicle=56.4516


# x=3783
# y=1445
# width_vehicle=22
# height_vehicle=11
# orientation_vehicle=-54.5543
        
    a = math.pow(math.cos(orientation_vehicle),2)/(2*math.pow(width_vehicle,2))+\
        math.pow(math.sin(orientation_vehicle),2)/(2*(math.pow(height_vehicle,2)))
    
    b = -1*(math.sin(orientation_vehicle*2))/4*math.pow(width_vehicle,2)+\
        (math.sin(orientation_vehicle*2)/4*math.pow(height_vehicle,2))
    
    c = math.pow(math.sin(orientation_vehicle),2)/2*math.pow((width_vehicle),2)+\
        math.pow(math.cos(orientation_vehicle),2)/2*math.pow(height_vehicle,2)

# a = (np.cos(theta)**2)/(2*sigma_x**2) + (np.sin(theta)**2)/(2*sigma_y**2)
# b = -(np.sin(2*theta))/(4*sigma_x**2) + (np.sin(2*theta))/(4*sigma_y**2)
# c = (np.sin(theta)**2)/(2*sigma_x**2) + (np.cos(theta)**2)/(2*sigma_y**2)

# a = (np.cos(theta)**2)/(2*sigma_x**2) + (np.sin(theta)**2)/(2*sigma_y**2)
# b = -(np.sin(2*theta))/(4*sigma_x**2) + (np.sin(2*theta))/(4*sigma_y**2)
# c = (np.sin(theta)**2)/(2*sigma_x**2) + (np.cos(theta)**2)/(2*sigma_y**2)
        
        
# a = math.cos(orientation_vehicle)/(2*width_vehicle)+\
#     math.sin(orientation_vehicle)/(2*(height_vehicle))

# b = -1*math.sin(orientation_vehicle*2)/4*width_vehicle+\
#     math.sin(orientation_vehicle*2)/4*height_vehicle

# c = math.sin(orientation_vehicle)/2*width_vehicle+\
#     math.cos(orientation_vehicle)/2*height_vehicle

# a=20
# b=40
# c=30


    generated_ground_truth=np.zeros((5616,3744))
    final=np.zeros((5616,3744))
    A=1;
    
        
        
        
    if 0<y<=3744 :
        
        if 3244<=y<=3744:
            
                iy=-500+y;
                ty=3744;
               
        if 0<y<500:
                iy=0;
                ty=y+500;
               
        if 500<=y<3244:
                iy=y-500;
                ty=y+500;
           
    
    
    if 0<=x<=5616 :
      
        if 5116<=x<=5616:
                ix=-500+x;
                tx=5616;
           
        if  0<x<500 :
                ix=0
                tx=x+500
               
        if 500<=x<5366:
                ix=x-500;
                tx=x+500;
           
    
#     # print(ix,'',tx)
#     # print(iy,'',ty)           
    
    
    
#     # 
#     # 
# # for i in range(0,5616):
# #   for j in range(0,3744):
    for i in range(ix,tx):
      for j in range(iy,ty):
          F =A*(np.exp( - (a*((i-x)**2) + 2*b*(i-x)*(j-y) + c*((j-y)**2))))
          generated_ground_truth[i][j]= F
    
    
    # # for i in range(0,5616):
    # #   for j in range(0,3744):     
    for i in range(ix,tx):
      for j in range(iy,ty):
          p = generated_ground_truth[i][j]/255
          final[i][j]=p
        # print(A*(np.exp(-(a*(np.power((i-x),2))+2*b*(i-x)*(j-y)+c*(np.power((j-y),2))))))
          # print(i)
          # print(j)               
        # np.where(generated_ground_truth==1)
# duration = 2000  # milliseconds
# freq = 640  # Hz
# winsound.Beep(freq, duration)

# final=generated_ground_truth
    # np.where(generated_ground_truth==1)
    return(final)
    
# plt.figure()
# plt.imshow(final)
# plt.colorbar()

# generated_ground_truth[1319][2338]
# import cv2
# cv2.imshow('image', generated_ground_truth)


# from PIL import Image
# #read the image

# im = Image.open(r"C:\Users\Payam_(cyrus)\Desktop\electric\3th term\neural networks\Vehicle Detection and Counting\MunichDatasetVehicleDetection-2015-old\Train\2012-04-26-Muenchen-Tunnel_4K0G0010.jpg")
# img = Image.fromarray(generated_ground_truth)
# #show image
# img.show()   
# im.show()
# return(final)


# hhh=grund_truths_calcuater_test(1330,2020\
#                                             ,30,30,\
#                                                 60)
# np.where(hhh==1)



# %%


import scipy.optimize as opt
import numpy as np
import pylab as plt
from PIL import Image
def twoD_Gaussian(xy, amplitude, xo, yo, sigma_x, sigma_y, theta):

    x, y = xy
    xo = float(xo)
    yo = float(yo)    
    a = (np.cos(theta)**2)/(2*sigma_x**2) + (np.sin(theta)**2)/(2*sigma_y**2)
    b = -(np.sin(2*theta))/(4*sigma_x**2) + (np.sin(2*theta))/(4*sigma_y**2)
    c = (np.sin(theta)**2)/(2*sigma_x**2) + (np.cos(theta)**2)/(2*sigma_y**2)
    
    g =  amplitude*np.exp( - (a*((x-xo)**2) + 2*b*(x-xo)*(y-yo) 
                            + c*((y-yo)**2)))
    Data = g.ravel()
    k=Data.reshape(3744,5616)
    return k

# -----------------------------------------------------------------------------
# def grund_truths_calcuater_test(x,y,width_vehicle,height_vehicle,orientation_vehicle):

# y = np.linspace(0, 5615, 5616)
# x = np.linspace(0, 3743, 3744)
# x, y = np.meshgrid(x,y)

# create data
# x0=1319
# y0=2338
# width_vehicle=35
# height_vehicle=11
# orientation_vehicle=56.4516

# x0=3783
# y0=1445
# width_vehicle=60
# height_vehicle=40
# orientation_vehicle=-54.5543

# data = twoD_Gaussian((x, y), 1, x0, y0,width_vehicle ,height_vehicle , orientation_vehicle)

# # # plot twoD_Gaussian data generated above

# plt.figure()
# plt.imshow(data)
# plt.colorbar()

# np.nonzero(data)

# im2 = Image.open(r"C:\Users\Payam_(cyrus)\Desktop\electric\3th term\neural networks\Vehicle Detection and Counting\MunichDatasetVehicleDetection-2015-old\Train\2012-04-26-Muenchen-Tunnel_4K0G0020.jpg")
# plt.figure()
# plt.imshow(im2)

def twoD_Gaussian2(xy, amplitude, xo, yo, sigma_x, sigma_y, theta):

    x, y = xy
    xo = float(xo)
    yo = float(yo)    
    a = (np.cos(theta)**2)/(2*sigma_x**2) + (np.sin(theta)**2)/(2*sigma_y**2)
    b = -(np.sin(2*theta))/(4*sigma_x**2) + (np.sin(2*theta))/(4*sigma_y**2)
    c = (np.sin(theta)**2)/(2*sigma_x**2) + (np.cos(theta)**2)/(2*sigma_y**2)
    
    g =  amplitude*np.exp( - (a*((x-xo)**2) + 2*b*(x-xo)*(y-yo) 
                            + c*((y-yo)**2)))
    Data = g.ravel()
    k=Data.reshape(3744,5616)
    return k

