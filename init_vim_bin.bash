#!/bin/bash

cp ~/grace/profile_backup/vimrc ~/.vimrc && echo "init_vim_SUCCESS"

#cp ~/grace/profile_backup/bashrc ~/.bashrc && echo "init_bash_SUCCESS"

mkdir ~/bin
cd ~/grace/_home_ed_bin && ./sync.bash && echo "init_home_ed_bin_SUCCESS"

#cd ~/grace && git config --global user.email "c_cstudy@126.com" && git config --global user.name "JiangEndian"

ssh-keygen -t rsa -C "c_cstudy@126.com"

echo "将以下id_rsa.pub内容复制到github的添加密钥上就可以push/pull了"
echo

cat ~/.ssh/id_rsa.pub

exit 0
