#!/bin/bash

while read -p "ContinueWithEnterOrCtrlC" && [[ $REPLY != 'exit' ]];do

    read -p "InputVideoUrl:" VideoUrl
    youtube-dl -F $VideoUrl

    read -p "InputVideoFormatNumber:" NumberOfVideoFormat
    youtube-dl -f $NumberOfVideoFormat $VideoUrl

    #read -p "InputVideoFormatNumber:" NumberOfVideoFormat
    #youtube-dl -f $NumberOfVideoFormat $VideoUrl
done
#-f best/worst/bestvideo/worstvideo/bestaudio/worstaudio
