#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

__author__ = 'Michael Liao'

'''
Deployment toolkit.
这家伙得在www的上级目录才行，因为它要进到当前目录下的www目录
'''

import os, re

from datetime import datetime
from fabric.api import *
import functools

#run = functools.partial(run, shell=False)

#服务器登录用户名
####################################
env.user = 'root'
env.sudo_user = 'root'
#env.hosts = ['192.168.1.117']
env.hosts = ['39.106.212.218']

db_user = 'www-data'
db_password = 'www-data'
####################################


_TAR_FILE = 'dist-awesome.tar.gz'

_REMOTE_TMP_TAR = '/tmp/%s' % _TAR_FILE

_REMOTE_BASE_DIR = '/srv/awesome'

def _current_path():
    return os.path.abspath('.')

def _now():
    return datetime.now().strftime('%y_%m_%d_%H.%M.%S')

#把远程数据库给打包复制至本地再删远程的打的包
def backup():
    '''
    Dump entire database on server and backup to local.
    '''
    dt = _now()
    f = 'backup_awesome_%s.sql' % dt
    with cd('/tmp'):
        run('mysqldump --user=%s --password=%s --skip-opt --add-drop-table --default-character-set=utf8 --quick awesome > %s' % (db_user, db_password, f))
        run('tar -czvf %s.tar.gz %s' % (f, f))
        get('%s.tar.gz' % f, '%s/backup/' % _current_path())
        run('rm -f %s' % f)
        run('rm -f %s.tar.gz' % f)

#打包任务
#这个完成后，在awesome-python3-webapp目录下运行fab build就打包
def build():
    '''
    Build dist package.
    '''
    includes = ['static', 'templates', 'transwarp', 'favicon.ico', '*.py']
    excludes = ['test', '.*', '*.pyc', '*.pyo']
    
    #先删除原有的打的包
    local('rm -f dist/%s' % _TAR_FILE)

    #拼成www的路径，并拼好打包命令
    #lcd把当前命令的目录认定为lcd指定的目录
    with lcd(os.path.join(_current_path(), 'www')):
        cmd = ['tar', '--dereference', '-czvf', '../dist/%s' % _TAR_FILE]
        cmd.extend(['--exclude=\'%s\'' % ex for ex in excludes])
        cmd.extend(includes)
        #fabric提供的local('command')来运行本地命令
        local(' '.join(cmd))

#然后，fab deploy就上传解包，各种事，就自动部署完成了
def deploy():
    #自动生成www附上日期的文件夹
    newdir = 'www_%s' % _now()

    #删除已有的tar文件,run函数执行的命令是在服务器上运行
    run('rm -f %s' % _REMOTE_TMP_TAR)
    #上传新的tar文件
    put('dist/%s' % _TAR_FILE, _REMOTE_TMP_TAR)
    #创建新目录
    #with cd和with lcd类似，服务器端设置为cd指定的目录
    with cd(_REMOTE_BASE_DIR):
        sudo('mkdir %s' % newdir) #命令需要sudo权限
    #解压到新目录
    with cd('%s/%s' % (_REMOTE_BASE_DIR, newdir)):
        sudo('tar -xzvf %s' % _REMOTE_TMP_TAR)
    #返回上级，重置软链接
    with cd(_REMOTE_BASE_DIR):
        sudo('rm -f www')
        sudo('ln -s %s www' % newdir)
        #把www的usr:group设置为了www-data...
        sudo('chown www-data:www-data www')
        sudo('chown -R www-data:www-data %s' % newdir)
    #再重启python服务器和nginx服务器(远程上的)
    with settings(warn_only=True):
        #supervisor只负责运行app.py，配置在/etc/supervisor/conf.d/
        #nginx配置文件在/etc/nginx/sites-available/
        #然后配置好了一个站点后，软链接配置文件至/etc/nginx/sites-enable里
        sudo('supervisorctl stop awesome')
        sudo('supervisorctl start awesome')
        sudo('/etc/init.d/nginx reload')

RE_FILES = re.compile('\r?\n')

def rollback():
    '''
    rollback to previous version
    '''
    with cd(_REMOTE_BASE_DIR):
        r = run('ls -p -1')
        files = [s[:-1] for s in RE_FILES.split(r) if s.startswith('www-') and s.endswith('/')]
        files.sort(cmp=lambda s1, s2: 1 if s1 < s2 else -1)
        r = run('ls -l www')
        ss = r.split(' -> ')
        if len(ss) != 2:
            print ('ERROR: \'www\' is not a symbol link.')
            return
        current = ss[1]
        print ('Found current symbol link points to: %s\n' % current)
        try:
            index = files.index(current)
        except ValueError, e:
            print ('ERROR: symbol link is invalid.')
            return
        if len(files) == index + 1:
            print ('ERROR: already the oldest version.')
        old = files[index + 1]
        print ('==================================================')
        for f in files:
            if f == current:
                print ('      Current ---> %s' % current)
            elif f == old:
                print ('  Rollback to ---> %s' % old)
            else:
                print ('                   %s' % f)
        print ('==================================================')
        print ('')
        yn = raw_input ('continue? y/N ')
        if yn != 'y' and yn != 'Y':
            print ('Rollback cancelled.')
            return
        print ('Start rollback...')
        sudo('rm -f www')
        sudo('ln -s %s www' % old)
        sudo('chown www-data:www-data www')
        with settings(warn_only=True):
            sudo('supervisorctl stop awesome')
            sudo('supervisorctl start awesome')
            sudo('/etc/init.d/nginx reload')
        print ('ROLLBACKED OK.')

#这个应该是把远程网站上的mysql库弄到本地的
def restore2local():
    '''
    Restore db to local
    '''
    backup_dir = os.path.join(_current_path(), 'backup')
    fs = os.listdir(backup_dir)
    files = [f for f in fs if f.startswith('backup-') and f.endswith('.sql.tar.gz')]
    files.sort(cmp=lambda s1, s2: 1 if s1 < s2 else -1)
    if len(files)==0:
        print 'No backup files found.'
        return
    print ('Found %s backup files:' % len(files))
    print ('==================================================')
    n = 0
    for f in files:
        print ('%s: %s' % (n, f))
        n = n + 1
    print ('==================================================')
    print ('')
    try:
        num = int(raw_input ('Restore file: '))
    except ValueError:
        print ('Invalid file number.')
        return
    restore_file = files[num]
    yn = raw_input('Restore file %s: %s? y/N ' % (num, restore_file))
    if yn != 'y' and yn != 'Y':
        print ('Restore cancelled.')
        return
    print ('Start restore to local database...')
    p = raw_input('Input mysql root password: ')
    sqls = [
        'drop database if exists awesome;',
        'create database awesome;',
        'grant select, insert, update, delete on awesome.* to \'%s\'@\'localhost\' identified by \'%s\';' % (db_user, db_password)
    ]
    for sql in sqls:
        local(r'mysql -uroot -p%s -e "%s"' % (p, sql))
    with lcd(backup_dir):
        local('tar zxvf %s' % restore_file)
    local(r'mysql -uroot -p%s awesome < backup/%s' % (p, restore_file[:-7]))
    with lcd(backup_dir):
        local('rm -f %s' % restore_file[:-7])
