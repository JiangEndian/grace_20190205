#!/bin/bash

cd /home/ed/grace_20190205/apps/new_gs && cp PlanDatabase.sqlite backup_db && ./show8.py
scp -p ed@47.244.31.34:/home/ed/apps/new_gs/PlanDatabase.sqlite /home/ed/grace_20190205/apps/new_gs/ && ./show8.py
read -p '请检查远程复制结果，如有错误请终止并从备份恢复'

cd /home/ed/grace_20190205/apps/language_voice_diction_korean && cp PlanDatabase.sqlite backup_db && ./show8.py
scp -p ed@47.244.31.34:/home/ed/apps/language_voice_diction_korean/PlanDatabase.sqlite /home/ed/grace_20190205/apps/language_voice_diction_korean/ && ./show8.py
read -p '请检查远程复制结果，如有错误请终止并从备份恢复'

cd /home/ed/grace_20190205/apps/language_voice_diction_english && cp PlanDatabase.sqlite backup_db && ./show8.py
scp -p ed@47.244.31.34:/home/ed/apps/language_voice_diction_english/PlanDatabase.sqlite /home/ed/grace_20190205/apps/language_voice_diction_english/ && ./show8.py
read -p '请检查远程复制结果，如有错误请终止并从备份恢复'

cd /home/ed/grace_20190205/apps/language_voice_diction_hebrew && cp PlanDatabase.sqlite backup_db && ./show8.py
scp -p ed@47.244.31.34:/home/ed/apps/language_voice_diction_hebrew/PlanDatabase.sqlite /home/ed/grace_20190205/apps/language_voice_diction_hebrew/ && ./show8.py
read -p '请检查远程复制结果，如有错误请终止并从备份恢复'






