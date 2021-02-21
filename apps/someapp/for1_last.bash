#!/bin/bash


ls_all()
{
for((i=1;i<23;i++));do
    ls 66_plain_revelation_$i.txt
done
}

ls_all
exit 0
