#!/bin/bash

name=$(date +%m%d_%H%M%S_%Y)

ls /media/ed/

#read -p "Copy the NAME of storage:"

#zip会把软链接的巨量音频也弄上好像。。。而且，tar快啊。哈哈哈哈
#cd /home/ed && tar -cf /media/ed/$REPLY/$name.tar /home/ed/grace_20190205/ && echo grace2tar_succese
cd /home/ed && tar -cf /media/ed/mint/$name.tar /home/ed/grace_20190205/ && echo grace2tar_succese  #最近就用这个卡，所以直接换上了

#echo jf3333333777|sudo -S cp /home/ed/ed.zip /var/www/html/ed.zip && echo cp2html_success

#cp /home/ed/$name.zip /home/ed/SeaDrive/ed_backup/ && echo zip2SeaDrive_success
#cp /home/ed/$name.zip /run/user/1000/gvfs/ftp:host=192.168.191.22,user=ll/endianbackup && echo zip2ftp_success

#cp /home/ed/$name.zip /media/ed/FAT_Backup && echo zip2FAT_Backup_success
#cp -ru /home/ed/grace /media/ed/FAT_Backup/ && echo cp_ru_2FAT_Backup_success

#检测UENDIAN移动U盘在不
#if [ -x /media/ed/UENDIAN ];then
    #cp /home/ed/$name.zip /media/ed/UENDIAN && echo zip2UENDIAN_success && umount /media/ed/UENDIAN && echo umounted
#else
    #echo UENDIAN不存在
#fi

#检测FTP远程在不
#if [ -x /run/user/1000/gvfs/ftp:host=192.168.191.222,user=jed/endian_back ];then
    #cp /home/ed/$name.zip /run/user/1000/gvfs/ftp:host=192.168.191.222,user=jed/endian_back && echo zip2FTP_success
#else
    #echo ftp不存在
#fi

#echo $name.zip

#df -h | grep media  #查看挂载到media的磁盘容量

exit 0
