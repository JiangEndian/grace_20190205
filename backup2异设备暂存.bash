#!/bin/bash

BACKUP='/media/ed/backup_tf'

rsync -av /home/ed/grace_20190205 $BACKUP && echo grace_20190205

rsync -av /home/ed/grace_voice_file $BACKUP && echo grace_voice_file

rsync -av /home/ed/图片 $BACKUP && echo 图片

rsync -av /home/ed/文档 $BACKUP && echo 文档

#rsync -av /home/ed/下载 $BACKUP && echo 下载

exit 0

