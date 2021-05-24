#!/bin/bash

sudo mysqldump -p --all-databases > allMysqlDatabase.sql

#to restore mysql database, use: mysql < allMysqlDatabase.sql
#you can enter mysql, use: source allMysqlDatabase.sql 
#如果是单个的数据库，则需要先创造个数据库，然后 mysql db1 < dump.sql
#哦，还可以直接 mysqladmin create db1这样的呢。
#当然可以进入mysql, CREATE DATABASE IF NOT EXISTS db1;USE db1;source dump.sql

