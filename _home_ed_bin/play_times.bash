#!/bin/bash

FILENAMES=''
for((i=0;i<$2;i++));do
    FILENAMES="$FILENAMES $1"
    #echo $FILENAMES
done

#exit 0

#global的话，哪里都能有效，那么，就不能打字了同时。。。
cvlc -R --global-key-play-pause 'p' --global-key-rate-faster-fine 'f' --global-key-rate-slower-fine 's' --no-repeat --play-and-exit $FILENAMES >/dev/null 2>&1 
#不global的话，就没有效果了。。。算了，不能打就不能打吧，反正就s和f这两个字符。。。
#cvlc -R --key-rate-faster-fine 'f' --key-rate-slower-fine 's' --no-repeat --play-and-exit $FILENAMES >/dev/null 2>&1 

exit 0
