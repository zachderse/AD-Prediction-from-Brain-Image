import shutil
import numpy as np 
import pandas as pd
import copy
import os
from PIL import Image, ImageDraw


#Make csv along with the data, may use this for later but most likely will use same directories as TensorFlow
#CSV allows for quick addition for other annotations if needed
AD_csv = {'filename' : [],'label' : []}
for i in range(400):
    #print("This is the file number ",i, ": ", end="")
    try:
        x = str(i).zfill(4)
        #print(x)
        file_name = ("/Users/zachderse//Desktop/cross_sectional_data/disc1/OAS1_"+x+"_MR1/OAS1_"+x+"_MR1.txt")
        f = open(file_name)
        textlines = f.readlines()
        CDR_num = str(textlines[6][14:17])
        CDR_num = CDR_num.strip()
                
        if CDR_num != '':
            AD_csv['filename'].append(x+"C_S.png")
            AD_csv['label'].append(CDR_num)
                
        orgfile = "/Users/zachderse//Desktop/cross_sectional_data/disc1/OAS1_"+x+"_MR1/FSL_SEG/OAS1_"+x+"_MR1_mpr_n4_anon_111_t88_masked_gfc_fseg_tra_90.gif"
        try:
            im = Image.open(orgfile)
            
            #im.save("/Users/zachderse//Desktop/cross_sectional_data/datasets/CDR_"+str(CDR_num)+"/"+x+"C_S.png")
            #print("copied successfully")
        except shutil.SameFileError:
            print("Source and destination represents the same file.")
    except:
        continue

AD_csv_df = pd.DataFrame(AD_csv)
AD_csv_df.to_csv('AD_CSV_labels')