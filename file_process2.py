# -*- coding: utf-8 -*-
"""
Created on Sat May 16 11:53:40 2020

@author: TARUN
"""


import pandas as pd
import os

path_d="data/processed_data/"
path_fd="data/processed_final_data/"
path_m="data/processed_data_motion/"

def get_entries(path):
    return os.listdir(path)

d_entries=get_entries(path_d)
m_entries=get_entries(path_m)

def sleep_stage_heart_beat_motion(hss,m):
    data=pd.read_csv(path_d+hss)
    m=pd.read_csv(path_m+m)
    j=0
    f1 = open(path_fd+hss, "w")
    f1.write("seconds,x,y,z,heartrate,sleep_stage\n")
    while(m['seconds'][j]<0):
            j+=1
    for i in range(len(data)):
        x1,y1,z1,c=0,0,0,0
        while(m['seconds'][j]<=data['seconds'][i]):
            j+=1
            x1+=m['x'][j]
            y1+=m['y'][j]
            z1+=m['z'][j]
            c+=1
        if(c<1):
            c+=1
        f1.write(str(data['seconds'][i])+','+str(x1/c)+','+str(y1/c)+','+str(z1/c)+','+str(data['heartrate'][i])+','+str(data['sleep_stage'][i])+'\n')
        
    f1.close()
    
for i in range(len(d_entries)):
    sleep_stage_heart_beat_motion(d_entries[i],m_entries[i])

        