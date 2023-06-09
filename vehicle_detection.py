# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 21:08:10 2022

@author: Payam_(cyrus)
"""
import glob
import os
import pandas as pd
import tensorflow as tf
from keras_preprocessing.image import ImageDataGenerator
import numpy as np
import grund_truths_calcuater
from grund_truths_calcuater import twoD_Gaussian,twoD_Gaussian2
import hamsayegi_mod
from hamsayegi_mod import image_feature
import winsound
import pylab as plt
import keras
from keras import models
from PIL import Image
import tensorflow as tf
import pandas as pd
from keras.models import Model,Sequential
from keras import layers
from keras.layers import Conv2D, MaxPool2D, BatchNormalization,Concatenate,activation,UpSampling2D
from numpy import array as narray
import cv2
import csv
import sklearn

import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from tensorflow.keras import Model, Input, regularizers
from tensorflow.keras.layers import Dense, Conv2D, MaxPool2D, UpSampling2D
from tensorflow.keras.callbacks import EarlyStopping
from keras.preprocessing import image
import glob
from tqdm import tqdm
import warnings;
warnings.filterwarnings('ignore')
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import load_img
from keras.layers import Input, Dense, concatenate

#read the image

# %%
# -----------------------------------------------------------------------------
# load data 

# im = Image.open(r"Images adresss")  
# im.show()

Image_Direct = r"MunichDatasetVehicleDetection-2015-old\Train"

files = os.listdir(Image_Direct)

for file in files:
    # make sure file is an image
    # if file.endswith('.jpg'):
      img_path = Image_Direct + file
      
images_Name_org=[]
for file in files:
    if file.endswith('.JPG'):
      img_path =  file
      images_Name_org.append(img_path)
        
featur_of_images=[]
my_files_path = glob.glob(r'MunichDatasetVehicleDetection-2015-old\Train\*.samp')
 
for file in range(0,len(my_files_path)):
    
    a=open(my_files_path[file],mode="r")
    print(a)
    
    content=a.read()
    h=[w for w in content.split() ]
    if h[0][0]=='@':
        a.readline()
        print(a.readline())
        a.readlines()
        a.seek(52)

        k=a.read()
        featur_of_images.append(k)
        print(a.read())
    else:
        a.readline()
        print(a.readline())
        a.readlines()
        a.seek(180)

        k=a.read()
        featur_of_images.append(k)
        print(a.read())
    a.close()  
        
# grouand Truth part==========================================================# 



listt_name_each_image=[]
num_fil_feature=[]
count_itr_file_img=[]
for i in range(0,len(featur_of_images)):
    listt_name_each_image.append((featur_of_images[i].split())[0])

name_of_img = list(dict.fromkeys(listt_name_each_image))    


for i in range(0,len(name_of_img)):
    count_itr_file_img.append(listt_name_each_image.count(name_of_img[i]))

all_feature_whit_out_name=[]
for i in range(0,len(featur_of_images)):
    all_feature_whit_out_name.append((featur_of_images[i])[80:])


feature_all_images=image_feature(all_feature_whit_out_name,count_itr_file_img,len(name_of_img))

all_feature_format_row_of_array=[]
for j in range(0,len(feature_all_images)):
    sss=np.concatenate((feature_all_images[j]))
    all_feature_format_row_of_array.append(sss)
 

# %% # formul (1)
list_ground_truth_each_img=[]

x = np.linspace(0, 5615, 5616)
y = np.linspace(0, 3743, 3744)
x, y = np.meshgrid(x,y)
for b in range(0,len(all_feature_format_row_of_array)):
    
    reshaped_img_1_feature=all_feature_format_row_of_array[b]
    
    l2=np.zeros((3744,5616))
    for j in range(0,len(reshaped_img_1_feature)):
        print(reshaped_img_1_feature[j][2],'',reshaped_img_1_feature[j][3],j,'=>',len(reshaped_img_1_feature))
        
        hhh=twoD_Gaussian2((x, y), 1,int(reshaped_img_1_feature[j][2]),int(reshaped_img_1_feature[j][3])\
                                      ,reshaped_img_1_feature[j][4],reshaped_img_1_feature[j][5],\
                                          reshaped_img_1_feature[j][6])
        l2=np.add(hhh,l2)    
            
        
        if j==len(reshaped_img_1_feature)-1:
                list_ground_truth_each_img.append(l2)
                

# figures of ground truthes

plt.figure()
plt.imshow(list_ground_truth_each_img[0])
plt.colorbar()


cv2.imshow('image', list_ground_truth_each_img[0])

img=Image.fromarray(list_ground_truth_each_img[1]*255)
img.show()

for i in list_ground_truth_each_img:
    from matplotlib import cm
    im = Image.fromarray(np.uint8(cm.gist_earth(i)*255))
    im.show()

# my_alarm
duration = 2000  # milliseconds
freq = 640  # Hz
winsound.Beep(freq, duration)



# cv2.imshow('image', list_ground_truths[0])


#%%============================================================================


# %%

all_images=[]
all_images_paths= []
for file in files:
    if file.endswith('.JPG'):
      img_path =  Image_Direct+ '\\' +file
      all_images_paths.append(img_path)

for s in range(len(all_images_paths)):
    for_siz=Image.open(all_images_paths[s])
    new_width  = 224
    new_height = 224
    for_siz = for_siz.resize((new_width, new_height), Image.ANTIALIAS)
    for_siz=np.array(for_siz)
    for_siz = for_siz.astype('float32')
    for_siz /= 255
    all_images.append(for_siz)
    
imaged_ground_trouth=[]
for cas in range(0,len(list_ground_truth_each_img)):
    # c=Image.fromarray(list_ground_truth_each_img[cas])
    c=np.resize(list_ground_truth_each_img[cas], (224,224))
    imaged_ground_trouth.append(c)
    
train = np.empty((8,224,224,3), dtype='uint16')
for num in range(0,8): 
    image2=all_images[num]
    train[num, :, :,:] = image2
    
train_label = np.empty((8,224,224), dtype='uint16')
for num in range(0,8): 
    t_label=imaged_ground_trouth[num]
    train_label[num, :, :] = t_label
    
testtt = np.empty((2,224,224,3), dtype='uint16')
for num in range(8,10): 
   t_image=all_images[num]
   testtt[num-8, :, :, :] =t_image

testtt_label = np.empty((2,224,224), dtype='uint16')
for num in range(8,10): 
   t_image_label=imaged_ground_trouth[num]
   testtt_label[num-8, :, :] =t_image_label   

t2=((train,train_label),(testtt,testtt_label))

# trian_set,label_set=sklearn.utils.shuffle(all_images,list_label_each_img)

# train, testtt = train_test_split(all_images, test_size=0.2, random_state=42, shuffle=True)
# train_label, testtt_label = train_test_split(list_label_each_img, test_size=0.2, random_state=42, shuffle=True)
# %%
batch_size = 1
epochs = 10
inChannel = 3
x, y = 224,224
input_img = Input(shape = (x, y, inChannel))


conv1=Conv2D(64, 3,padding='same',activation='relu')(input_img)
conv1=Conv2D(64, 3, padding='same',activation='relu')(conv1)
conv1=MaxPool2D()(conv1)

conv2=Conv2D(128, 3,padding='same', activation='relu')(conv1)
conv2=Conv2D(128, 3, padding='same',activation='relu')(conv2)
conv2=MaxPool2D()(conv2)

conv3=Conv2D(256, 3,padding='same', activation='relu')(conv2)
conv3=Conv2D(256, 3, padding='same',activation='relu')(conv3)
conv3=Conv2D(256, 3, padding='same',activation='relu')(conv3)
conv3=MaxPool2D()(conv3)

conv4=Conv2D(512, 3,padding='same', activation='relu')(conv3)
conv4=Conv2D(512, 3, padding='same',activation='relu')(conv4)
conv4=Conv2D(512, 3, padding='same',activation='relu')(conv4)
conv4=MaxPool2D()(conv4)

conv5=Conv2D(512, 3,padding='same', activation='relu')(conv4)
conv5=Conv2D(512, 3, padding='same',activation='relu')(conv5)
conv5=Conv2D(512, 3, padding='same',activation='relu')(conv5)
up_sampling_con5=UpSampling2D()(conv5)

D1=Conv2D(256, 3,padding='same', activation='relu')(up_sampling_con5)   
D1=BatchNormalization()(D1)
D1=Conv2D(256, 3, padding='same',activation='relu')(D1)
D1=BatchNormalization()(D1)

D2=Conv2D(128, 3, padding='same',activation='relu')(D1)
D2=BatchNormalization()(D2)
D2=Conv2D(128, 3, padding='same',activation='relu')(D2)
D2=BatchNormalization()(D2)

D3=Conv2D(64, 3, padding='same',activation='relu')(D2)
D3=BatchNormalization()(D3)
D3=Conv2D(64, 3, padding='same',activation='relu')(D3)
D3=BatchNormalization()(D3)

deconv1_concat=Concatenate()([D1,up_sampling_con5])
deconv1=Conv2D(256, 3,padding='same',activation='relu')(deconv1_concat)
deconv1=BatchNormalization()(deconv1)
deconv1=Conv2D(256, 3,padding='same',activation='relu')(deconv1)
deconv1=BatchNormalization()(deconv1)
up_sampling_deconv1=UpSampling2D()(deconv1)

deconv2=Concatenate()([D2,deconv1])
deconv2=Conv2D(256, 3,padding='same',activation='relu')(deconv2)
deconv2=BatchNormalization()(deconv2)
deconv2=Conv2D(256, 3,padding='same',activation='relu')(deconv2)
deconv2=BatchNormalization()(deconv2)
up_sampling_deconv2=UpSampling2D()(deconv2)

deconv3=Concatenate()([D3,deconv2])
deconv3=Conv2D(256, 3,padding='same',activation='relu')(up_sampling_deconv2)
deconv3=BatchNormalization()(deconv3)
deconv3=Conv2D(256, 3,padding='same',activation='relu')(deconv3)
deconv3=BatchNormalization()(deconv3)
up_sampling_deconv3=UpSampling2D()(deconv3)

deconv4=Conv2D(256, 3,padding='same',activation='relu')(up_sampling_deconv3)
deconv4=BatchNormalization()(deconv4)
deconv4=Conv2D(256, 3,padding='same',activation='relu')(deconv4)
deconv4=BatchNormalization()(deconv4)

up_sampling_deconv3=UpSampling2D()(deconv4)
decov5=tf.keras.layers.Conv2D(1, 1, activation='linear')(up_sampling_deconv3)

my_model= Model(input_img,decov5)
my_model.summary()


my_model.compile(optimizer='RMSprop', loss = 'mean_squared_error', metrics=['accuracy'])


monitor = EarlyStopping(monitor='val_loss', min_delta=1e-3, verbose=1, mode='auto',
        restore_best_weights=True)


trainig_run = my_model.fit(train, train_label, batch_size=batch_size,
                                    epochs=epochs,verbose=1,validation_data=(testtt, testtt_label))



