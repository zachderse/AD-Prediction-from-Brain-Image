import os
import shutil  
from PIL import Image

 
# Assigning the images to files that are related to the metadata of AD rank

for i in range(1,400):
    #print("This is the file number ",i, ": ", end="")
    try:
        x = str(i).zfill(4)
        print(x)
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

        #dest = "/Users/zachderse//Desktop/cross_sectional_data/CDR_"+str(CDR_num)+"/"+x+"C_S.gif"
        try:
            #shutil.copy(orgfile, dest)
            im = Image.open(orgfile)
            im.save("/Users/zachderse//Desktop/cross_sectional_data/datasets/CDR_"+str(CDR_num)+"/"+x+"C_S.png")
            print("copied successfully")
        except shutil.SameFileError:
            print("Source and destination represents the same file.")




    except:
        continue

