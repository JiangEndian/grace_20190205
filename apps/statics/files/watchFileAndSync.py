#!/usr/bin/env python3
from watchdog.observers import Observer
from watchdog.events import *
from MyPython3 import *
import time

localFile = 'temp4submit'
remoteLocation = 'ed@47.244.31.34:/home/ed/grace_20190205/apps/statics/files/'
scpCmd = f'scp {localFile} {remoteLocation}'

def syncFile():
    print(scpCmd)
    runsyscmd('date')
    runsyscmd(scpCmd)

class FileEventHandler(FileSystemEventHandler):
    def __init__(self):
        FileSystemEventHandler.__init__(self)

    def on_moved(self, event):
        if event.is_directory:
            pass
            #print('directory moved from {0} to {1}'.format(event.src_path, event.dest_path))
        else:
            #print('file moved from {0} to {1}'.format(event.src_path, event.dest_path))
            if event.dest_path.endswith(localFile):
                print('file moved from {0} to {1}'.format(event.src_path, event.dest_path))
                syncFile()
                

    #def on_created(self, event):
        #if event.is_directory:
            #print('directory created: {0}'.format(event.src_path))
        #else:
            #print('file created: {0}'.format(event.src_path))

    #def on_deleted(self, event):
        #if event.is_directory:
            #print('directory deleted: {0}'.format(event.src_path))
        #else:
            #print('file deleted: {0}'.format(event.src_path))
        
    #def on_modifiedd(self, event):
        #if event.is_directory:
            #print('directory modified: {0}'.format(event.src_path))
        #else:
            #print('file modified: {0}'.format(event.src_path))

observer = Observer()
event_handler = FileEventHandler()
observer.schedule(event_handler, '/home/ed/', False) #True是循环的
observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()

