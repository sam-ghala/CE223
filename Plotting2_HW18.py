# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 15:32:35 2019

@author: sjghalayini
"""
#%% Task 1
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('data_tasks.xlsx',sheet_name='task1')
x = range(9)
temp = []
tempp = []
for y in df.values[:,1]:
    temp.append(y)
for yy in df.values[:,2]:
    tempp.append(yy)
plt.plot(x,temp,c='red',)
for x in range(9):
    plt.errorbar(x,temp[x],yerr=tempp[x],fmt = "ks--",linewidth = 1.5,capsize=4,capthick = 1)
plt.legend(['Standard Deviation'],numpoints=1,loc=('upper left'))
plt.xlabel("Time (min)",fontsize = 10)
plt.ylabel("Temperature (C)",fontsize = 10)
plt.title("Temperature vs. Time with Standard Deviation",fontsize = 14)
plt.yticks([0,5,10,15,20,25])
plt.savefig('filename.png',dpi = 600)

plt.figure()
plt.bar(df.values[:,0],df.values[:,1],yerr=tempp,align='center',ecolor='red',capsize=10)
plt.title("Temperature vs. Time with Standard Deviation",fontsize = 14)
plt.xlabel("Time (min)",fontsize = 10)
plt.ylabel("Temperature (C)",fontsize = 10)
plt.savefig('filename0.png',dpi = 600)

#%% Task 2
import pandas as pd
import matplotlib.pyplot as plt
plt.figure()
df1 = pd.read_excel('data_tasks.xlsx',sheet_name='task2')
x = range(6)
temp = []
tempp = []
temppp = []
e = []
ee = []
eee = []
for y in df1.values[1:,1]:
    temp.append(y)
for yy in df1.values[1:,3]:
    tempp.append(yy)
for yyy in df1.values[1:,5]:
    temppp.append(yyy)
for er in df1.values[1:,2]:
    e.append(er)
for err in df1.values[1:,4]:
    ee.append(err)
for errr in df1.values[1:,6]:
    eee.append(errr)
    
plt.figure()
plt.plot(x,temp,c='red')
plt.title("Las Vegas Temperature vs. Time with Standard Deviation")
plt.xlabel("Time(min)",fontsize = 10)
plt.ylabel("Temperature(C)",fontsize = 10)
for xx in range(6):
    plt.errorbar(xx,temp[xx],yerr=e[xx],fmt = "k",linewidth = 1.5,capsize=4,capthick = 1)
plt.yticks([0,10,20,30,40,50,60,70])
plt.xticks([1,2,3,4,5,6])
plt.legend(["Standard Deviation"],numpoints=1,loc=('upper left'))
plt.savefig('filename2.png',dpi = 600)

plt.figure()
plt.plot(x,tempp,c='red')
plt.title("Durango Temperature vs. Time with Standard Deviation")
plt.xlabel("Time(min)",fontsize = 10)
plt.ylabel("Temperature(C)",fontsize = 10)
for xx in range(6):
    plt.errorbar(xx,tempp[xx],yerr=ee[xx],fmt = "k",linewidth = 1.5,capsize=4,capthick = 1)
plt.yticks([0,5,10,15,20,25,30,35,40])
plt.xticks([1,2,3,4,5,6])
plt.legend(["Standard Deviation"],numpoints=1,loc=('upper left'))
plt.savefig('filename2.png',dpi = 600)

plt.figure()
plt.plot(x,temppp,c='red')
plt.title("Denver Temperature vs. Time with Standard Deviation")
plt.xlabel("Time(min)",fontsize = 10)
plt.ylabel("Temperature(C)",fontsize = 10)
for xx in range(6):
    plt.errorbar(xx,temppp[xx],yerr=eee[xx],fmt = "k",linewidth = 1.5,capsize=4,capthick = 1)
plt.yticks([0,5,10,15,20,25])
plt.xticks([1,2,3,4,5,6])
plt.legend(["Standard Deviation"],numpoints=1,loc=('upper left'))
plt.savefig('filename2.png',dpi = 600)
#########################################
plt.figure()
plt.bar(df1.values[1:,0],df1.values[1:,1],yerr=df1.values[1:,2],align='center',ecolor='red',capsize=10)
plt.title("Las Vegas Temperature vs. Time with Standard Deviation",fontsize = 14)
plt.xlabel("Time (min)",fontsize = 10)
plt.ylabel("Temperature (C)",fontsize = 10)
plt.legend(["Standard Deviation"],numpoints=1,loc=('upper left'))
plt.savefig('filename0.png',dpi = 600)

plt.figure()
plt.bar(df1.values[1:,0],df1.values[1:,3],yerr=df1.values[1:,4],align='center',ecolor='red',capsize=10)
plt.title("Durango Temperature vs. Time with Standard Deviation",fontsize = 14)
plt.xlabel("Time (min)",fontsize = 10)
plt.ylabel("Temperature (C)",fontsize = 10)
plt.legend(["Standard Deviation"],numpoints=1,loc=('upper left'))
plt.savefig('filename0.png',dpi = 600)

plt.figure()
plt.bar(df1.values[1:,0],df1.values[1:,5],yerr=df1.values[1:,6],align='center',ecolor='red',capsize=10)
plt.title("Denver Temperature vs. Time with Standard Deviation",fontsize = 14)
plt.xlabel("Time (min)",fontsize = 10)
plt.ylabel("Temperature (C)",fontsize = 10)
plt.legend(["Standard Deviation"],numpoints=1,loc=('upper left'))
plt.savefig('filename0.png',dpi = 600)
















