#!/usr/bin/python
#adapted from Mumfordbrainstats. bold=func. %s=string replacement. %d=number replacement
#This script creates symbolic link for the reg directory in the .feat folder

import glob
import os
import sys
import subprocess

path = '/Volumes/KATYA5GBA/HCP_Gambling_RESULTSevent'

func_files = glob.glob('%s/*/tfMRI_GAMBLING_[LR][RL]/lev1_DMNppi.feat'%(path))

#For each sub and each run do the following:
for cur_sub in list(func_files):
	print(cur_sub)
	#set dir name
	cur_dir = os.path.dirname(cur_sub)

        os.system('mkdir %s/reg'%(cur_sub))
        os.system('ln -s $FSLDIR/etc/flirtsch/ident.mat %s/reg/example_func2standard.mat'%(cur_sub))
        os.system('ln -s $FSLDIR/etc/flirtsch/ident.mat %s/reg/standard2example_func.mat'%(cur_sub))
        os.system('ln -s $FSLDIR/data/standard/MNI152_T1_2mm_brain.nii.gz %s/reg/standard.nii.gz'%(cur_sub))
