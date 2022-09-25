# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 11:25:41 2020

@author: yama4971
"""

import glob
import numpy
import subprocess
import os, shutil
import xarray as xr
import json


def cdo_fldmean(fold_in,file_in,fold_out,renew_files):
    """
    Masks different regions of fields with a regular lon/lat grid
    """
    for f in file_in:
        p = subprocess.Popen("ubuntu run cdo fldmean '"+fold_in+"/"+f+".maskregion.nc' /home/mayan1991/"+f+'.fldmean.nc', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in p.stdout.readlines():
            print(line) 
        shutil.move('C:\\Users\\yama4971\\AppData\\Local\\Packages\\CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc\\LocalState\\rootfs\\home\\mayan1991\\'+f+'.fldmean.nc',fold_out+'\\'+f+'.fldmean.nc')

def cdo_yearmean(fold_in,file_in,fold_out,renew_files):
    """
    This module calulate the yearly mean.
    """
    for f in file_in: 
        p = subprocess.Popen("ubuntu run cdo yearmean"+" '"+fold_in+"/"+f+".fldmean.nc' /home/mayan1991/yearmean.nc", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in p.stdout.readlines():
            print(line)
        shutil.move('C:\\Users\\yama4971\\AppData\\Local\\Packages\\CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc\\LocalState\\rootfs\\home\\mayan1991\\yearmean.nc',fold_out+'\\'+f+'.yearmean.nc') 

def cdo_summermean(fold_in,file_in,fold_out,renew_files):
    """
    This module calulate the yearly mean.
    """
    for f in file_in: 
        p = subprocess.Popen("ubuntu run cdo yearmean -selmon,6,7,8"+" '"+fold_in+"/"+f+".fldmean.nc' /home/mayan1991/summermean.nc", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in p.stdout.readlines():
            print(line)
        shutil.move('C:\\Users\\yama4971\\AppData\\Local\\Packages\\CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc\\LocalState\\rootfs\\home\\mayan1991\\summermean.nc',fold_out+'\\'+f+'.summermean.nc') 

def cdo_springmean(fold_in,file_in,fold_out,renew_files):
    """
    This module calulate the yearly mean.
    """
    for f in file_in: 
        p = subprocess.Popen("ubuntu run cdo yearmean -selmon,3,4,5"+" '"+fold_in+"/"+f+".fldmean.nc' /home/mayan1991/springmean.nc", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in p.stdout.readlines():
            print(line)
        shutil.move('C:\\Users\\yama4971\\AppData\\Local\\Packages\\CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc\\LocalState\\rootfs\\home\\mayan1991\\springmean.nc',fold_out+'\\'+f+'.springmean.nc') 

def cdo_autumnmean(fold_in,file_in,fold_out,renew_files):
    """
    This module calulate the yearly mean.
    """
    for f in file_in: 
        p = subprocess.Popen("ubuntu run cdo yearmean -selmon,9,10,11"+" '"+fold_in+"/"+f+".fldmean.nc' /home/mayan1991/autumnmean.nc", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in p.stdout.readlines():
            print(line)
        shutil.move('C:\\Users\\yama4971\\AppData\\Local\\Packages\\CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc\\LocalState\\rootfs\\home\\mayan1991\\autumnmean.nc',fold_out+'\\'+f+'.autumnmean.nc') 

def cdo_wintermean(fold_in,file_in,fold_out,renew_files):
    """
    This module calulate the winter mean.
    """
    for f in file_in: 
        p = subprocess.Popen("ubuntu run cdo timselmean,3,11,9"+" '"+fold_in+"/"+f+".fldmean.nc' /home/mayan1991/wintermean.nc", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in p.stdout.readlines():
            print(line)
        shutil.move('C:\\Users\\yama4971\\AppData\\Local\\Packages\\CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc\\LocalState\\rootfs\\home\\mayan1991\\wintermean.nc',fold_out+'\\'+f+'.wintermean.nc') 

def cdo_yearmin(fold_in,file_in,fold_out,renew_files):
    """
    This module calulate the winter mean.
    """
    for f in file_in: 
        p = subprocess.Popen("ubuntu run cdo yearmin"+" '"+fold_in+"/"+f+".fldmean.nc' /home/mayan1991/yearmin.nc", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in p.stdout.readlines():
            print(line)
        shutil.move('C:\\Users\\yama4971\\AppData\\Local\\Packages\\CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc\\LocalState\\rootfs\\home\\mayan1991\\yearmin.nc',fold_out+'\\'+f+'.yearmin.nc') 

def cdo_yearmax(fold_in,file_in,fold_out,renew_files):
    """
    This module calulate the winter mean.
    """
    for f in file_in: 
        p = subprocess.Popen("ubuntu run cdo yearmax"+" '"+fold_in+"/"+f+".fldmean.nc' /home/mayan1991/yearmax.nc", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in p.stdout.readlines():
            print(line)
        shutil.move('C:\\Users\\yama4971\\AppData\\Local\\Packages\\CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc\\LocalState\\rootfs\\home\\mayan1991\\yearmax.nc',fold_out+'\\'+f+'.yearmax.nc') 

def cdo_runmean(fold_in,file_in,fold_out,renew_files):
    """
    This module calulate the winter mean.
    """
    for f in file_in: 
        p = subprocess.Popen("ubuntu run cdo runmean,3"+" '"+fold_in+"/"+f+".fldmean.nc' /home/mayan1991/runmean.nc", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in p.stdout.readlines():
            print(line)
        shutil.move('C:\\Users\\yama4971\\AppData\\Local\\Packages\\CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc\\LocalState\\rootfs\\home\\mayan1991\\runmean.nc',fold_out+'\\'+f+'.runmean.nc') 

def cdo_runmean_max(fold_in,file_in,fold_out,renew_files):
    """
    This module calulate the winter mean.
    """
    for f in file_in: 
        p = subprocess.Popen("ubuntu run cdo yearmax"+" '"+fold_in+"/"+f+".runmean.nc' /home/mayan1991/runmean_max.nc", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in p.stdout.readlines():
            print(line)
        shutil.move('C:\\Users\\yama4971\\AppData\\Local\\Packages\\CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc\\LocalState\\rootfs\\home\\mayan1991\\runmean_max.nc',fold_out+'\\'+f+'.runmean_max.nc') 

def cdo_runmean_min(fold_in,file_in,fold_out,renew_files):
    """
    This module calulate the winter mean.
    """
    for f in file_in: 
        p = subprocess.Popen("ubuntu run cdo timselmin,12,6"+" '"+fold_in+"/"+f+".runmean.nc' /home/mayan1991/runmean_min.nc", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in p.stdout.readlines():
            print(line)
        shutil.move('C:\\Users\\yama4971\\AppData\\Local\\Packages\\CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc\\LocalState\\rootfs\\home\\mayan1991\\runmean_min.nc',fold_out+'\\'+f+'.runmean_min.nc') 


countries=['russia','all','finland_russia','norway_finland_russia','sweden_finland']
country=countries[0]  
                                         
fold_out='C:\\Users\\yama4971\\Desktop\\his_data\\tmp\\'+country+'\\tmp' 
fold_in='/mnt/c/Users/yama4971/Desktop/his_data/tmp/'+country+'/tmp' 
file_in=['tmp_1961_2019']
renew_files=True
cdo_fldmean(fold_in,file_in,fold_out,renew_files)
cdo_yearmean(fold_in,file_in,fold_out,renew_files)
cdo_springmean(fold_in,file_in,fold_out,renew_files)
cdo_summermean(fold_in,file_in,fold_out,renew_files)
cdo_autumnmean(fold_in,file_in,fold_out,renew_files)
cdo_wintermean(fold_in,file_in,fold_out,renew_files)
cdo_yearmin(fold_in,file_in,fold_out,renew_files)
cdo_yearmax(fold_in,file_in,fold_out,renew_files)
cdo_runmean(fold_in,file_in,fold_out,renew_files)
cdo_runmean_max(fold_in,file_in,fold_out,renew_files)
cdo_runmean_min(fold_in,file_in,fold_out,renew_files)

'''
data = numpy.zeros((59,1))   
ds = xr.open_dataset('C:\\Users\\yama4971\\Desktop\\his_data\\tmp\\'+country+'\\tmp\\tmp_1961_2019.yearmean.nc') 
tmp = ds['tmp'].values 
ds.close()
for j in range(0,59):
    data[j][0]=tmp[j,0,0]
    
data2 = numpy.zeros((59,1))   
ds2 = xr.open_dataset('C:\\Users\\yama4971\\Desktop\\his_data\\tmp\\'+country+'\\tmp\\tmp_1961_2019.summermean.nc') 
tmp2 = ds2['tmp'].values 
ds2.close()
for j in range(0,59):
    data2[j][0]=tmp2[j,0,0]
    
data3 = numpy.zeros((59,1))   
ds3 = xr.open_dataset('C:\\Users\\yama4971\\Desktop\\his_data\\tmp\\'+country+'\\tmp\\tmp_1961_2019.wintermean.nc') 
tmp3 = ds3['tmp'].values 
ds3.close()
for j in range(0,59):
    data3[j][0]=tmp3[j,0,0]
'''
