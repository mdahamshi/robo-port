#!/usr/bin/env python2

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
        subProcess("pbme \"Attack detetcted !\"")
        return
    arguments = message.split('::')
    print "get args: ",arguments
    command = "/usr/bin/" + getCommand(arguments[0].lower()) 
    if command == "restart":
        subProcess('play-atte')
        replaceMe("pushServer")
        
    arguments[0] = command
    print "new process args: ",arguments
    newProgram = subProcess(arguments)


def getCommand(message):
    return {
        'radio': "start-radio"
        , 'test': "env > /data/tmp/ee"
        , 'stop': "stop-mplayer"
        , 's': "stop-mplayer"
        , 'quran': "start-quran"
        , '+': "volume-up"
        , '-': "volume-down"
        , 'down': "volume-down"
	    , 'play': "play-atte"
        , 'up': "volume-up"
        , 'restart': "restart"
        , 'imhere': "play-arrive"
        , 'speak': "robo-speak"
    }.get(message, "pbme \"pushServer: wrong command received !\";echo "+message+" > /data/tmp/err")

def getEnvo(message):
    return {
        'shell': "os"
    }.get(message, "")
def chuser(user_uid, user_gid):
    os.setgid(user_gid)
    os.setuid(user_uid)

def replaceMe(newProcess):
    os.execv('/usr/bin/' + newProcess , sys.argv)

def subProcess(sub):
    subprocess.Popen(sub, shell=True \
    , preexec_fn=chuser(pw_record.pw_uid, pw_record.pw_gid),env=env)  
  
