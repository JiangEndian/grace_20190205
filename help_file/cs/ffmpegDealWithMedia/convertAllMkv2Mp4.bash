#!/bin/bash

for f in *.mkv; do ffmpeg -i "$f" -codec copy "${f%.mkv}.mp4"; done


