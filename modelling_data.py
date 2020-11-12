# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 12:00:04 2020
DT20206769917
@author: TARUN
"""

import pandas as pd
import os
import csv


with open('data/data_sleep.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Id", "HRBS", "HRD0", "HRD1", "HRD2", "HRD3", "HRD5", "HRAS", "TTB", "ST0", "ST1", "ST2", "ST3", "ST5", "TST", "SLPC"])
        
path_ls="data/processed_data_labeled_sleep/"
path_hr="data/processed_data_heart_rate/"

def get_entries(path):
    return os.listdir(path)

ls_entries=get_entries(path_ls)
hr_entries=get_entries(path_hr)


def sleep_stage_range(labeled_sleep):
    data=pd.read_csv(path_ls+labeled_sleep)
    f=0
    s=data['sleep_stage'][0]
    l0=[[],[]]
    l1=[[],[]]
    l2=[[],[]]
    l3=[[],[]]
    l5=[[],[]]
    if(s==0):
        l0[f].append(data['seconds'][0])
    elif(s==1):
        l1[f].append(data['seconds'][0])
    elif(s==2):
        l2[f].append(data['seconds'][0])
    elif(s==3):
        l3[f].append(data['seconds'][0])
    else:
        l5[f].append(data['seconds'][0])
        
    f=1
    n=len(data)
    for i in range(1, n):
        if(data['sleep_stage'][i]!=s):
            if(s==0):
                l0[1].append(data['seconds'][i-1])
            elif(s==1):
                l1[1].append(data['seconds'][i-1])
            elif(s==2):
                l2[1].append(data['seconds'][i-1])
            elif(s==3):
                l3[1].append(data['seconds'][i-1])
            else:
                l5[1].append(data['seconds'][i-1])
            s=data['sleep_stage'][i]
            if(s==0):
                l0[0].append(data['seconds'][i])
            elif(s==1):
                l1[0].append(data['seconds'][i])
            elif(s==2):
                l2[0].append(data['seconds'][i])
            elif(s==3):
                l3[0].append(data['seconds'][i])
            else:
                l5[0].append(data['seconds'][i])
            
    if(s==0):
        l0[1].append(data['seconds'][n-1])
    elif(s==1):
        l1[1].append(data['seconds'][n-1])
    elif(s==2):
        l2[1].append(data['seconds'][n-1])
    elif(s==3):
        l3[1].append(data['seconds'][n-1])
    else:
        l5[1].append(data['seconds'][n-1])
       
    m=[[]]
    l=[]
    for i in range(len(l0[0])):
        l.append(l0[0][i])
        l.append(l0[1][i])
        l.append(0)
        m.append(l)
        l=[]
    for i in range(len(l1[0])):
        l=[]
        l.append(l1[0][i])
        l.append(l1[1][i])
        l.append(1)
        m.append(l)
    for i in range(len(l2[0])):
        l=[]
        l.append(l2[0][i])
        l.append(l2[1][i])
        l.append(2)
        m.append(l)
    for i in range(len(l3[0])):
        l=[]
        l.append(l3[0][i])
        l.append(l3[1][i])
        l.append(3)
        m.append(l)
    for i in range(len(l5[0])):
        l=[]
        l.append(l5[0][i])
        l.append(l5[1][i])
        l.append(5)
        m.append(l)    
    
    m=m[1:]
    return sorted(m)


def labeled_sleep_hr(labeled_sleep, heartrate):
    m=sleep_stage_range(labeled_sleep)
    data=pd.read_csv(path_hr+heartrate)
    f1 = open("data/processed_data/"+labeled_sleep[:-7]+".txt", "w")
    s=[]
    h=[]
    k=0
    r=0
    a=[]
    sa=[]
    c=0
    f1.write("seconds,heartrate,sleep_stage\n")
    for i in range(len(data)):
        if(data['seconds'][i]<0):
            s.append(data['seconds'][i])
            h.append(data['heartrate'][i])
        else:
            if(data['seconds'][i]<=m[k][1]):
                c=c+1
                r+=data['heartrate'][i]
                f1.write(str(data['seconds'][i])+','+str(data['heartrate'][i])+','+str(m[k][2])+'\n')
            elif data['seconds'][i]>m[-1][1]:
                if(data['seconds'][i-1]<=m[-1][1]):
                    m[k].append(r)
                    m[k].append(c)
                    f1.write(str(data['seconds'][i-1])+','+str(data['heartrate'][i-1])+','+str(m[-1][2])+'\n')
                a.append(data['seconds'][i])
                sa.append(data['heartrate'][i])
            else:
                m[k].append(r)
                m[k].append(c)
                r=data['heartrate'][i]
                f1.write(str(data['seconds'][i])+','+str(data['heartrate'][i])+','+str(m[k][2])+'\n')
                k=k+1
                c=1
    bh=sum(h)/len(h)
    ah=sum(sa)/len(sa)
    
    for i in m:
        if(i[-1]!=0):
            i.append(i[-2]/i[-1])
    
    h=[0,0,0,0,0]
    t=[0,0,0,0,0]
    c=[0,0,0,0,0]
    for i in m:
        if(i[2]==0):
            h[0]+=i[-1]
            c[0]+=1
            t[0]+=i[1]-i[0]+30
        elif(i[2]==1):
            h[1]+=i[-1]
            c[1]+=1
            t[1]+=i[1]-i[0]+30
        elif(i[2]==2):
            h[2]+=i[-1]
            c[2]+=1
            t[2]+=i[1]-i[0]+30
        elif(i[2]==3):
            h[3]+=i[-1]
            c[3]+=1
            t[3]+=i[1]-i[0]+30
        else:
            h[4]+=i[-1]
            c[4]+=1
            t[4]+=i[1]-i[0]+30
       
    for i in range(len(h)):
        if(c[i]!=0):
            h[i]=h[i]/c[i]
    ttb=sum(t)
    tst=ttb-t[0]
    sleep_condition=""
    if tst>=21600 and (t[4]/tst)*100>=20 and (tst/ttb)*100>=85:
        sleep_condition="GOOD"
    elif (t[4]/tst)*100>=20 and (tst/ttb)*100>=85:
        sleep_condition="MODERATE"
    else:
        sleep_condition="BAD"
    with open('data/data_sleep.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([labeled_sleep[:-7], bh, h[0], h[1], h[2], h[3], h[4], ah, ttb, t[0], t[1], t[2], t[3], t[4], tst, sleep_condition])
                
        
    f1.close()   
    
    
for i in range(len(ls_entries)):
    labeled_sleep_hr(ls_entries[i],hr_entries[i])
    

