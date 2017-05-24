#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import subprocess
import os
import sys
import pwd  
import signal

global program
global chars
chars = set('\;\&\|')
program = -1
pw_record = pwd.getpwnam('mohammad')
env = os.environ.copy()
env['HOME'] = pw_record.pw_dir
env['LOGNAME'] = pw_record.pw_name
env['USER'] = pw_record.pw_name
env['USERNAME'] = pw_record.pw_name

def parse(message):
    """This function parse a push message and run the corresponding command """
    global program
    global chars
    if any((c in chars) for c in message):
        subprocess.Popen("pbme \"Attack detetcted !\"", shell=True \
        , preexec_fn=chuser(pw_record.pw_uid, pw_record.pw_gid),env=env)
        return
    arguments = message.split('::')
    command = getCommand(arguments[0].lower())
    if command == "restart":
        os.execv("/data/archbkp/robot/pushbullet/push.py", sys.argv)
    arguments[0] = command
    print command
    program = subprocess.Popen(arguments, shell=True \
    , preexec_fn=chuser(pw_record.pw_uid, pw_record.pw_gid),env=env)


def getCommand(message):
    return {
        'radio': "start-radio &> /dev/null"
        , 'test': "env > /data/tmp/ee"
        , 'stop': "stop-mplayer"
        , 's': "stop-mplayer"
        , 'quran': "start-quran &> /dev/null"
        , '+': "volume-up"
        , '-': "volume-down"
        , 'down': "volume-down"
	    , 'play': "play-atte"
        , 'up': "volume-up"
        , "restart": "restart"
        , "speak": "robo-speak"
    }.get(message, "pbme \"pushServer: wrong command received !\"")

def getEnvo(message):
    return {
        'shell': "os"
    }.get(message, "")
def chuser(user_uid, user_gid):
    os.setgid(user_gid)
    os.setuid(user_uid)
  
