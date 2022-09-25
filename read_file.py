# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 13:24:54 2020

@author: yama4971
"""

import numpy
import xarray as xr
import pandas as pd

country='bor_cluster_hh'

data_tmp = numpy.zeros((59,13))  

varis=['yearmean','wintermean','springmean','summermean','autumnmean','yearmax','yearmin'] 
for i,k in zip(varis,range(0,13)):
    ds = xr.open_dataset('C:\\Users\\yama4971\\Desktop\\his_data\\tmp\\'+country+'\\tmp\\tmp_1961_2019.'+i+'.nc') 
    tmp= ds['tmp'].values  
    ds.close()
    for j in range(0,59):
        data_tmp[j][k]=tmp[j,0,0]
        
varis_2=['runmean_max','runmean_min']
for i,k in zip(varis_2,[7,10]):
    ds = xr.open_dataset('C:\\Users\\yama4971\\Desktop\\his_data\\tmp\\'+country+'\\tmp\\tmp_1961_2019.'+i+'.nc') 
    tmp= ds['tmp'].values  
    time=ds['tmp'].time.values
    year=pd.to_datetime(time).year
    month=pd.to_datetime(time).month
    ds.close()
    for j in range(0,59):
        data_tmp[j][k]=year[j]
        data_tmp[j][k+1]=month[j]
        data_tmp[j][k+2]=tmp[j,0,0]


data_pre = numpy.zeros((59,13))  

varis=['yearsum','winterpre','springpre','summerpre','autumnpre','yearmax','yearmin'] 
for i,k in zip(varis,range(0,13)):
    ds = xr.open_dataset('C:\\Users\\yama4971\\Desktop\\his_data\\pre\\'+country+'\\pre\\pre_1961_2019.'+i+'.nc') 
    pre= ds['pre'].values  
    ds.close()
    for j in range(0,59):
        data_pre[j][k]=pre[j,0,0]
        
varis_2=['runsum_max','runsum_min']
for i,k in zip(varis_2,[7,10]):
    ds = xr.open_dataset('C:\\Users\\yama4971\\Desktop\\his_data\\pre\\'+country+'\\pre\\pre_1961_2019.'+i+'.nc') 
    pre= ds['pre'].values  
    time=ds['pre'].time.values
    year=pd.to_datetime(time).year
    month=pd.to_datetime(time).month
    ds.close()
    for j in range(0,59):
        data_pre[j][k]=year[j]
        data_pre[j][k+1]=month[j]
        data_pre[j][k+2]=pre[j,0,0]
    
