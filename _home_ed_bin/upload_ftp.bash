#!/bin/bash

ftpFILE='upload.ftp'

echo "open 192.168.191.222" > $ftpFILE
echo "user jed jed" >> $ftpFILE
echo "bin" >> $ftpFILE
echo "prompt" >> $ftpFILE
echo "put $1 $2" >> $ftpFILE
echo "ls" >> $ftpFILE
echo "bye" >> $ftpFILE

ftp -n < $ftpFILE

rm $ftpFILE

exit 0
