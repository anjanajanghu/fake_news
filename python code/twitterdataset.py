# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 18:28:29 2019

@author: Anju
"""
import numpy as np
import pandas as pd
sourcefile =pd.read_csv("twitterid.txt");
pf=sourcefile['TwitterId']
count=0;
for x in pf:
    try:
        label ="twitter15/tree/"+str(x)+".txt"
        print(label)
        file = open(label, "r")
        lines = file.read().split("\n")
        size=len(lines)-1        
        # define length of columns
        twitterid = ["" for x in range(size)]
        userid = ["" for x in range(size)]
        timestamp = ["" for x in range(size)]
        share = ["" for x in range(size)]
        ii=0
        for l in lines:
            try:
                if l == '\n':
                    break;
                values = l.split("]->[")
                firstpart=values[1].split(",")
                user=firstpart[0].split("'")
                tweet=firstpart[1].split("'")
                time=firstpart[2].split("'")    
                userid[ii]=user[1]
                twitterid[ii]=tweet[1]
                timestamp[ii]=time[1]
                if timestamp[ii]=='0.0':
                    share[ii]=0;
                else:
                    share[ii]=1; 
                ii=ii+1
            except:
                print(l)
    
        df ={ 'userid':userid,
              'twitterid':twitterid,
              'timestamp':timestamp,
              'share':share
             }
        df= pd.DataFrame(df)
        count=count+1
        if count==1 :
            df.to_csv("dataset4.txt");
        else:
            df.to_csv("dataset4.txt",mode='a', header=False);
    except Exception as e: 
        print(e)

np.random.choice([0, 1], size=(10,), p=[0.34,0.66])
# 0,1  1/3,2/3  twitterdataset --- 2/3 1/3  twitterdataset1  ------ 0.75 0.25 datset2  ------- 0.90, 0.10 dataset3    --- 0.99,0.01 dataset4
label ="dataset4.txt"
file = open(label, "r")
lines = file.read().split("\n")
s=len(lines)-2

a=np.random.choice([0, 1], size=s, p=[0.99,0.01])
#a=np.random.binomial(1, frac, size=s)

files = label
df = pd.read_csv(files)
df = df.convert_objects(convert_numeric=True)
    #until here, the code is running fine
    #now i wanted to add a new column in a specific index with all value =10           
df.insert(4,'flag',a)
df.to_csv(files)

