#!/bin/bash

#rsync -rvpP /home/ed/grace_voice_file 47.244.31.34:/home/ed/ #显示每个太烦了

rsync -avP --exclude-from='excluded' 47.244.31.34:/home/ed/grace_voice_file /home/ed/grace_voice_file 
#rsync -avP --exclude 'grace_voice_file/20201012_en_long' /home/ed/grace_voice_file 47.244.31.34:/home/ed/ #只需要等待

