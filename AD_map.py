import os
import shutil  
from PIL import Image


# Assigning the images to files that are related to the metadata of AD rank


package_num = 1
for i in range(1,42):
    #print("This is the file number ",i, ": ", end="")
    try:
        x = str(i).zfill(4)
        file_name = ("/Users/zachderse//Desktop/cross_sectional_data/disc1/OAS1_"+x+"_MR1/OAS1_"+x+"_MR1.txt")
        f = open(file_name)
        textlines = f.readlines()
        CDR_num = str(textlines[6][14:17])
        CDR_num = CDR_num.strip()
        
        match CDR_num:
            case "0":
                print("0")
            case "0.5":
                print("0.5")
            case "1":
                print("1")
            case "2":
                print("2")
  
            case _ :
                print("none available")
        
        
        #sets up directories
        
        orgfile = "/Users/zachderse//Desktop/cross_sectional_data/disc1/OAS1_"+x+"_MR1/FSL_SEG/OAS1_"+x+"_MR1_mpr_n4_anon_111_t88_masked_gfc_fseg_tra_90.gif"
        dest = "/Users/zachderse//Desktop/cross_sectional_data/CDR_"+str(CDR_num)+"/"+x+"C_S.gif"
        try:
            shutil.copy(orgfile, dest)
            print("copied successfully")
        except shutil.SameFileError:
            print("Source and destination represents the same file.")
            
            
            
        
    except:
        continue

from PIL import Image


import numpy as np
import os
import PIL
import PIL.Image
import tensorflow as tf

im = Image.open("0028C_S.jpg")
pix = np.array(im)
print(pix.shape)


#set the dimensions
im_ht = 256
im_wd = 256
bat_sz = 2
#training set
ds_train = tf.keras.preprocessing.image_dataset_from_directory(
    '/Users/zachderse//Desktop/cross_sectional_data/datasets/', 
    labels="inferred",
    label_mode = "categorical", 
    color_mode = "grayscale", 
    batch_size = bat_sz,
    seed = 123, 
    validation_split = .1, 
    image_size = (im_ht,im_wd),
    subset = "training")

#test set
ds_valid = tf.keras.preprocessing.image_dataset_from_directory(
    '/Users/zachderse//Desktop/cross_sectional_data/datasets/', 
    labels="inferred",
    label_mode = "categorical", 
    color_mode = "grayscale", 
    batch_size = bat_sz,
    seed = 123, 
    validation_split = .1, 
    image_size = (im_ht,im_wd),
    subset = "validation")




class_names = ds_train.class_names
print(class_names)


AUTOTUNE = tf.data.AUTOTUNE

ds_train = ds_train.cache().prefetch(buffer_size=AUTOTUNE)
ds_valid = ds_valid.cache().prefetch(buffer_size=AUTOTUNE)




normalization_layer = tf.keras.layers.Rescaling(1./255)

normalized_ds = ds_train.map(lambda x, y: (normalization_layer(x), y))

image_batch, labels_batch = next(iter(normalized_ds))

first_image = image_batch[0]
print(np.min(first_image), np.max(first_image))

num_classes = 4

model = tf.keras.Sequential([
  tf.keras.layers.Rescaling(1./255),
  tf.keras.layers.Conv2D(16, 3, activation='relu'),
  tf.keras.layers.MaxPooling2D(),
  tf.keras.layers.Conv2D(32, 3, activation='relu'),
  tf.keras.layers.MaxPooling2D(),
  tf.keras.layers.Conv2D(64, 3, activation='relu'),
  tf.keras.layers.MaxPooling2D(),
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dense(num_classes)
])

model.compile(
  optimizer='adam',
  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
  metrics=['accuracy'])

model.summary()

model.fit(
  ds_train,
  validation_data=ds_valid,
  epochs=3
)

