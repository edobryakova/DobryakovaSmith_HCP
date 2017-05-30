#!/usr/bin/env/python
#this script takes the text file with 12 columns of movement (Movement_regressors.txt) and copies the first 6 motion parameters into a new file (motionfile_6columns.txt).

import glob, sys, os

path='/Volumes/KATYA5GBA/HCP_Gambling_eventRelated/*/MNINonLinear/Results/tfMRI_GAMBLING_*/'
motionfiles=glob.glob('%s/Movement_regressors.txt'%(path))

for file in list(motionfiles):
	motionfile=open(file, 'r')
	parentFolder=os.path.abspath(os.path.join(file, os.pardir))
	motionfile_6columns = open ('%s/motionfile_6columns.txt'%parentFolder, 'w')
	for row in motionfile:
		columns = row.strip().split()
		motionfile_6columns.write("\t".join(columns[:6])+"\n")
	motionfile.close()
	motionfile_6columns.close()


