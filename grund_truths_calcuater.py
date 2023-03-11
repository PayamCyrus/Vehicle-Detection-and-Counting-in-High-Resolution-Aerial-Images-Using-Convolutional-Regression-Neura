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
    

        
    a = math.pow(math.cos(orientation_vehicle),2)/(2*math.pow(width_vehicle,2))+\
        math.pow(math.sin(orientation_vehicle),2)/(2*(math.pow(height_vehicle,2)))
    
    b = -1*(math.sin(orientation_vehicle*2))/4*math.pow(width_vehicle,2)+\
        (math.sin(orientation_vehicle*2)/4*math.pow(height_vehicle,2))
    
    c = math.pow(math.sin(orientation_vehicle),2)/2*math.pow((width_vehicle),2)+\
        math.pow(math.cos(orientation_vehicle),2)/2*math.pow(height_vehicle,2)



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
    
    
    

    for i in range(ix,tx):
      for j in range(iy,ty):
          F =A*(np.exp( - (a*((i-x)**2) + 2*b*(i-x)*(j-y) + c*((j-y)**2))))
          generated_ground_truth[i][j]= F
    
 
    for i in range(ix,tx):
      for j in range(iy,ty):
          p = generated_ground_truth[i][j]/255
          final[i][j]=p

    return(final)
    



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

