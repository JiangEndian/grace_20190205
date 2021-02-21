#!/bin/bash

ssh-keygen -t rsa

cd ~/.ssh && cat id_rsa.pub

echo "Please append this key to the authorized_keys file which located in .ssh"


