#!/bin/bash

echo "/home/ed/grace_voice_file/WorshipSongs/下的文件名"
SRC="47.244.31.34:3927/static/grace_voice/WorshipSongs/$1"
chrome $SRC || chromium-browser $SRC || firefox $SRC

