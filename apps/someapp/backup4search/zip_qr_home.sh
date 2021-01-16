#!/bin/bash
#User be zip this dir...

BACKUPFILE=backup_$(date +%m%d%Y)
ENDIAN=${1:-$BACKUPFILE}
zip -q -r /home/endian/$ENDIAN.zip /home/endian/恩典/
