#!/usr/bin/env python
# Linux Recycle
# Author Steven
# Modify 2013-12-18

import time,sys,os,shutil
recy_path = "/data/Recycle/"
now = time.strftime('%Y%m%d_%H_%M_%S',time.localtime(time.time()))

if not os.path.isdir(recy_path):
	os.makedirs(recy_path)

para = sys.argv[1:]
if '-f' in para:
	para.remove('-f')
if '-r' in para:
	para.remove('-r')
if '-rf' in para:
	para.remove('-rf')

deny = ['/usr','/usr/','/var','/var/','/root','/root/','/etc','/etc/','/home','/home/','/proc','/proc/','/boot','/boot/','/bin','/bin/','/sbin','/sbin/','/lib','/lib/','/lib64','/lib64/','/']

for p in tuple(para):
	if p in deny:
		para.remove(p)
		print "Dangerous command: %s" % p

if not para:
	sys.exit('Nothing to run.')

for f in para:

	try:
		if '/' not in f:
			recy_file = "%s/%s_%s" % (recy_path,now,f)
			shutil.move(f,recy_file)
		else:
			path = os.path.dirname(f)
			file = os.path.basename(f)
			if file == "":
				file = path.split('/')[-1]

			recy_file = "%s/%s_%s" % (recy_path,now,file)
			shutil.move(f,recy_file)
	except Exception,e:
		print e

