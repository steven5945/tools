#!/bin/sh
# Author Steven
# Modify 20131218

if [ `whoami` != 'root' ];then
        echo "Must be root run this scripts!!" >> /var/log/messages
        exit
fi

dirpath=/data/Recycle/
ago=`date -d "-15 day" +%Y%m%d`

if [ ! -d $dirpath ];then
	echo "This path [${dirpath}] not exist, please check." >> /var/log/messages
	exit
fi

for i in `ls $dirpath`
do
	# Get datestamp and check it. For example: 20130304_09_54_25_ld.lock 
	datestamp=`echo $i | awk -F'_' '{print $1}'`
	check=`echo "$datestamp" | grep "^[0-9]\{8\}$"`

	if [[ `echo $check` -ne "" ]];then
		# Remove old files.
		if [ "$datestamp" -lt "$ago" ];then
			/bin/rm -rf $dirpath/$i	
		fi
	fi
done
