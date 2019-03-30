# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 18:02:58 2019

@author: Anju
"""

import numpy as np
import pandas as pd

datavar=pd.read_csv("twitter15/label.txt");

label ="twitter15/label.txt"
file = open(label, "r")
lines = file.read().split("\n")

# define length of columns
label = ["" for x in range(len(lines))]
twitterid = ["" for x in range(len(lines))]
 
ii=0
for l in lines:
    values = l.split(":")
    label[ii]=values[0]
    twitterid[ii]=values[1]
    ii=ii+1
    
df ={ 'label':label,
      'TwitterId':twitterid
     }
df= pd.DataFrame(df)
df.to_csv("twitterid.txt");