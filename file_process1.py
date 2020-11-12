# -*- coding: utf-8 -*-
"""
Created on Wed May 13 10:54:03 2020

@author: TARUN
"""

import os

path_ls="data/labels/"
path_hr="data/heart_rate/"
path_m="data/motion/"

def get_entries(path):
    return os.listdir(path)

ls_entries=get_entries(path_ls)
hr_entries=get_entries(path_hr)
m_entries=get_entries(path_m)

def process_file_labled_sleep(file):
    newpath="data/processed_data_labeled_sleep/"
    f = open(path_ls+file, "r")
    newfile=file[:-17]+"ls.txt"
    f1 = open(newpath+newfile, "w")
    f1.write("seconds"+','+"sleep_stage\n")
    
    while True:
        line = f.readline()
        if not line:
            break
        s=line.split(' ')
        f1.write(s[0]+','+s[1])
    
    f.close()
    f1.close()
    
def process_file_heartrate(file):
    newpath="data/processed_data_heart_rate/"
    f = open(path_hr+file, "r")
    newfile=file[:-13]+"hr.txt"
    f1 = open(newpath+newfile, "w")
    f1.write("seconds"+','+"heartrate\n")
    
    while True:
        line = f.readline()
        if not line:
            break
        f1.write(line)
        
    f.close()
    f1.close()
    
def process_file_motion(file):
    newpath="data/processed_data_motion/"
    f = open(path_m+file, "r")
    newfile=file[:-16]+"m.txt"
    f1 = open(newpath+newfile, "w")
    f1.write("seconds"+','+"x"+','+'y'+','+'z\n')    
    while True:
        line = f.readline()
        if not line:
            break
        s=line.split(' ')
        f1.write(s[0]+','+s[1]+','+s[2]+','+s[3])
        
    f.close()
    f1.close()
  
for i in hr_entries:
    process_file_heartrate(i)

for i in ls_entries:
    process_file_labled_sleep(i)
    
for i in m_entries:
    process_file_motion(i)

