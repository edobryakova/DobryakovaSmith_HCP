#!/usr/bin/python
 
# This creates the level2 fsf's using template for ER design
 
import os
import glob
 
studydir = '/Volumes/KATYA5GBA/HCP_Gambling_RESULTSevent'
 
fsfdir='/Users/edobryakova/Documents/HCPgambling_templates/lev2_fsf'
 
 
subdirs=glob.glob("%s/*/tfMRI_GAMBLING_*"%(studydir))
 
for dir in list(subdirs):
	splitdir = dir.split('/')
	splitdir_sub = splitdir[4]  # You will need to edit this
	subnum=splitdir_sub[:]    # You also may need to edit this
  	subfeats=glob.glob("%s/lev1.feat"%(dir))
	print(dir+"->"+str(len(subfeats)))
  	if len(subfeats)==1:  # Add your own second loop for 2 feat cases
    		print(subnum)
    		replacements = {'SUBNUM':subnum}
    		with open("/Users/edobryakova/Documents/HCPgambling_templates/lev2ER_template.fsf") as infile: 
      			with open("%s/lev2_ER_%s.fsf"%(fsfdir, subnum), 'w') as outfile:
          			for line in infile:
            				for src, target in replacements.iteritems():
              					line = line.replace(src, target)
            				outfile.write(line)
