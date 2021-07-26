#!/bin/bash

ffmpeg -i $1 -i $2 -c copy -c:s mov_text $3

