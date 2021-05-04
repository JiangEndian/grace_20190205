#!/bin/bash

read -p "InputFolder: "

cd $REPLY && ls -lh && echo $REPLY

while true;do
    read -p "InputFileNumber: "
    cvlc --global-key-quit 'q' --play-and-exit "wavFile10$REPLY.wav" > /dev/null 2>&1
done


