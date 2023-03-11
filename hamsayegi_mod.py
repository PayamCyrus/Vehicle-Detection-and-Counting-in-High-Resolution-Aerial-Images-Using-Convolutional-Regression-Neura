# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 19:40:26 2023

@author: Payam_(cyrus)
"""
import numpy as np
def image_feature(all_feature_whit_out_name_i,count_itr_file_img_i,number_of_img):
    
# number_of_img=10
    shomaresatr_featur_img=np.zeros([1,1])
   
    now=[]
    past=[]
    for i in range(0,number_of_img):
       shomaresatr_featur_img=np.add(shomaresatr_featur_img,count_itr_file_img_i[i])
       now.append(shomaresatr_featur_img)
    past.append(0)
    for j in range(0,9):
     past.append(now[j])
   
   
    feature_all_img_=[]
    for k in range(0,len(past)):
       ss=all_feature_whit_out_name_i[int(past[k]):int(now[k])]
       list_emergency=[]
       feature_all_img_.append(list_emergency)
       for j in ss:
           kl=j.split()
           numLines = int(np.floor(len(kl)/7))
           
           p=np.array(kl)
           reshaped=np.reshape(p,[numLines,7])
           reshape_array=np.float32(reshaped)
           list_emergency.append(reshape_array)
    return(feature_all_img_)


