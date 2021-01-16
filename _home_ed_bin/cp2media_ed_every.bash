#!/bin/bash

if [ -z $1 ];then
    echo '$1 is Null, exit...'
    exit 0
fi

to_dir=$(ls /media/ed/)

if [ -z $to_dir ];then
    echo '/media/ed/ is empty, exit...'
    exit 0
fi

echo $to_dir && read -p 'Enter2Continue...'

for dir in $to_dir;do

    new_dir='/media/ed/'$dir
    
    for i;do
        cp $i $new_dir && echo "cp_ed $1 $new_dir" 
    done
    umount $new_dir && echo "umount_ed $new_dir"

done

exit 0

