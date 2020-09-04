# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 05:15:28 2020

@author: Jatin
"""

import os
import pandas as pd
import cv2
path="./Raw Data"
Files=os.listdir(path)
data={'name':[],'age':[],"gender":[],"ethnicity":[]}


for f in Files:
    file=f.split("_")
    if len(file)==4:
        if int(file[0])<75:
            data['name'].append(f)
            data['age'].append(int(file[0]))
            data['gender'].append(int(file[1]))
            data['ethnicity'].append(int(file[2]))

# Creating dat frame of valuue  
data_csv=pd.DataFrame(data)

#bining the agee  values
bins=[0,10,20,50,120]
names=["Child","Teenagers","Adults","Old"] #labels for the bins
data_csv['age groups']= pd.cut(data_csv['age'],bins,labels=names)

# printing the top 5 values
print(data_csv.head())

# writings to the csv
data_csv.to_csv("Face_data.csv",index=False)
    
    
    


            
        
        

