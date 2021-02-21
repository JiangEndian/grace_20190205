#!/bin/bash

play2times(){
    cvlc -R --no-repeat --play-and-exit $1 > /dev/null 2>&1
    cvlc -R --no-repeat --play-and-exit $1 > /dev/null 2>&1
}

NOW_DIR=$(basename $(pwd))

for file_name;do
    clear
    echo *${file_name}*
    grep -A 9 ${file_name}: /home/ed/grace/apps/plan_endian/ben/*${NOW_DIR}* |grep .
    play2times *${file_name}*

done

exit 0
