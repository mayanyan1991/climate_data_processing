# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 12:00:27 2020

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

def cdo_summerpre(fold_in,file_in,fold_out,renew_files):#imput file should be rainfall
    """
    This module select and sum up the value of periond June, July, August.
    """
    for f in file_in: 
        p = subprocess.Popen("ubuntu run cdo yearsum -selmon,6,7,8"+" '"+fold_in+"/"+f+".fldmean.nc' /home/mayan1991/summerpre.nc", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in p.stdout.readlines():
            print(line)
        shutil.move('C:\\Users\\yama4971\\AppData\\Local\\Packages\\CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc\\LocalState\\rootfs\\home\\mayan1991\\summerpre.nc',fold_out+'\\'+f+'.summerpre.nc') 

def cdo_yearsum(fold_in,file_in,fold_out,renew_files):#imput file should be rainfall
    """
    This module calulate the yearly mean.
    """
    for f in file_in: 
        p = subprocess.Popen("ubuntu run cdo yearsum"+" '"+fold_in+"/"+f+".fldmean.nc' /home/mayan1991/yearsum.nc", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in p.stdout.readlines():
            print(line)
        shutil.move('C:\\Users\\yama4971\\AppData\\Local\\Packages\\CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc\\LocalState\\rootfs\\home\\mayan1991\\yearsum.nc',fold_out+'\\'+f+'.yearsum.nc') 

def cdo_winterpre(fold_in,file_in,fold_out,renew_files):#imput file should be rainfall
    """
    This module select and sum up the value of periond Dec,Jan,Feb.
    """
    for f in file_in: 
        p = subprocess.Popen("ubuntu run cdo timselsum,3,11,9"+" '"+fold_in+"/"+f+".fldmean.nc' /home/mayan1991/winterpre.nc", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in p.stdout.readlines():
            print(line)
        shutil.move('C:\\Users\\yama4971\\AppData\\Local\\Packages\\CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc\\LocalState\\rootfs\\home\\mayan1991\\winterpre.nc',fold_out+'\\'+f+'.winterpre.nc') 

def cdo_springpre(fold_in,file_in,fold_out,renew_files):
    """
    This module calulate the yearly mean.
    """
    for f in file_in: 
        p = subprocess.Popen("ubuntu run cdo yearsum -selmon,3,4,5"+" '"+fold_in+"/"+f+".fldmean.nc' /home/mayan1991/springpre.nc", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in p.stdout.readlines():
            print(line)
        shutil.move('C:\\Users\\yama4971\\AppData\\Local\\Packages\\CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc\\LocalState\\rootfs\\home\\mayan1991\\springpre.nc',fold_out+'\\'+f+'.springpre.nc') 

def cdo_autumnpre(fold_in,file_in,fold_out,renew_files):
    """
    This module calulate the yearly mean.
    """
    for f in file_in: 
        p = subprocess.Popen("ubuntu run cdo yearsum -selmon,9,10,11"+" '"+fold_in+"/"+f+".fldmean.nc' /home/mayan1991/autumnpre.nc", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in p.stdout.readlines():
            print(line)
        shutil.move('C:\\Users\\yama4971\\AppData\\Local\\Packages\\CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc\\LocalState\\rootfs\\home\\mayan1991\\autumnpre.nc',fold_out+'\\'+f+'.autumnpre.nc') 

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

def cdo_runsum(fold_in,file_in,fold_out,renew_files):
    """
    This module calulate the winter mean.
    """
    for f in file_in: 
        p = subprocess.Popen("ubuntu run cdo runsum,3"+" '"+fold_in+"/"+f+".fldmean.nc' /home/mayan1991/runsum.nc", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in p.stdout.readlines():
            print(line)
        shutil.move('C:\\Users\\yama4971\\AppData\\Local\\Packages\\CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc\\LocalState\\rootfs\\home\\mayan1991\\runsum.nc',fold_out+'\\'+f+'.runsum.nc') 

def cdo_runsum_max(fold_in,file_in,fold_out,renew_files):
    """
    This module calulate the winter mean.
    """
    for f in file_in: 
        p = subprocess.Popen("ubuntu run cdo yearmax"+" '"+fold_in+"/"+f+".runsum.nc' /home/mayan1991/runsum_max.nc", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in p.stdout.readlines():
            print(line)
        shutil.move('C:\\Users\\yama4971\\AppData\\Local\\Packages\\CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc\\LocalState\\rootfs\\home\\mayan1991\\runsum_max.nc',fold_out+'\\'+f+'.runsum_max.nc') 

def cdo_runsum_min(fold_in,file_in,fold_out,renew_files):
    """
    This module calulate the winter mean.
    """
    for f in file_in: 
        p = subprocess.Popen("ubuntu run cdo timselmin,12,7"+" '"+fold_in+"/"+f+".runsum.nc' /home/mayan1991/runsum_min.nc", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in p.stdout.readlines():
            print(line)
        shutil.move('C:\\Users\\yama4971\\AppData\\Local\\Packages\\CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc\\LocalState\\rootfs\\home\\mayan1991\\runsum_min.nc',fold_out+'\\'+f+'.runsum_min.nc') 



countries=['russia','all','finland_russia','norway_finland_russia','sweden_finland']
country=countries[0] 

renew_files=True  
file_in=['pre_1961_2019']                                           
fold_out='C:\\Users\\yama4971\\Desktop\\his_data\\pre\\'+country+'\\pre'  
fold_in='/mnt/c/Users/yama4971/Desktop/his_data/pre/'+country+'/pre'   
cdo_fldmean(fold_in,file_in,fold_out,renew_files)
cdo_yearsum(fold_in,file_in,fold_out,renew_files)
cdo_summerpre(fold_in,file_in,fold_out,renew_files)
cdo_springpre(fold_in,file_in,fold_out,renew_files)
cdo_winterpre(fold_in,file_in,fold_out,renew_files)
cdo_autumnpre(fold_in,file_in,fold_out,renew_files)
cdo_yearmin(fold_in,file_in,fold_out,renew_files)
cdo_yearmax(fold_in,file_in,fold_out,renew_files)
cdo_runsum(fold_in,file_in,fold_out,renew_files)
cdo_runsum_max(fold_in,file_in,fold_out,renew_files)
cdo_runsum_min(fold_in,file_in,fold_out,renew_files)