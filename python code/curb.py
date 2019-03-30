# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 23:09:33 2019

@author: Anju
"""
import pandas as pd
import numpy as np
import operator
from collections import defaultdict

def setflagCount():
    flaged={}
    for row in df.itertuples(index=True, name='Pandas'):
        twitterid = getattr(row, "twitterid")
        flag = getattr(row, "flag")
        if flag==1:
            flagcount=flaged.get(twitterid)
            if flagcount==None:                
                d1={twitterid : 1 }
            else:
                flagcount=int(flagcount)+1
                d1={twitterid : flagcount}
            flaged.update(d1)
        else:
            flagcount=flaged.get(twitterid)
            if flagcount==None:                
                d1={twitterid : 0 }
                flaged.update(d1)
                        
    return flaged;   

def history():
    historyData={}
    for row in df.itertuples(index=True, name='Pandas'):
        twitterid = getattr(row, "twitterid")
        storycount=historyData.get(twitterid)
        if storycount==None:                
            d1={twitterid : 1 }
        else:
            storycount=int(storycount)+1
            d1={twitterid : storycount}
        historyData.update(d1)
           
    return historyData;

def getintensities(histData):
    intensities={}
    totalevents=sum(histData.values())
    for key, value in histData.items():
        intensity_x= int(value)/totalevents
        d1={key : intensity_x}
        intensities.update(d1)
    return intensities 
  
def fakenews(intensity,flaged):
    exposure={}
    exposure={k: intensity[k]*flaged[k] for k in flaged}       
    return exposure

def markverified(twitterid) :
    verified.update({twitterid: 'verified'})
    return 0;

# remove verified news from data
def removenew(twitterid) :
    del gHistoryData[twitterid]
    del intensities[twitterid]
    del flaged[twitterid]
    return 1


datset=pd.read_csv("dataset4.txt")
#convert timestamp to positive
datset['timestamp'] = datset['timestamp'].abs()  
#remove duplicate values
datset=datset.drop_duplicates(subset=['userid', 'twitterid','timestamp'])
df=datset.sort_values(by=['timestamp']) 
exposured={}
verified={}
flaged=setflagCount()
gHistoryData=history()
intensities=getintensities(gHistoryData)
exposured=fakenews(intensities,flaged)



ds = [intensities, exposured,flaged,gHistoryData]
d = {}
for k,v in intensities.items():
    d[k] = tuple(d[k] for d in ds)

df=pd.DataFrame.from_dict(d, orient='index', columns=['intensities', 'exposure', 'flag','historyevents'])
  
df= pd.DataFrame(df)
df.insert(2, "result", "5") 
df.to_csv("result4.txt");
#twitterid=max(exposured.items(), key=operator.itemgetter(1))[0] 
#markverified(twitterid)
#removenew(twitterid)

#df ={ 'twitterid':twitterid,
#      'timestamp':timestamp,
#      'share':share
 #    }
#df= pd.DataFrame(df)
#df.to_csv("result1.txt");



