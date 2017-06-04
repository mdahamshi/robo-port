#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import subprocess
import os
import sys
import pwd  
import signal
import codecs
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
env['LANG'] = 'en_US.UTF-8'
def parse(message):
    """This function parse a push message and run the corresponding command """
    global program
    global chars
    if any((c in chars) for c in message):
        subProcess("pbme \"Attack detetcted !\"")
        return
    arguments = message.split('::')

    if arguments[0] == 'speak' or arguments[0] == 'speakr':
        if len(arguments) > 1:
            speakHelper(arguments[1],arguments[0])
        return
    
    command = getCommand(arguments[0].lower().strip()) 
    if command == "pberr":
        arguments.apend(arguments[0])
    if command == "restart":
        subProcess('/usr/bin/play-atte')
        replaceMe("pushServer")
    if os.path.isfile('./'+command):
        arguments[0] =  './' +  command 
    else:
        arguments[0] =  '/usr/bin/' +  command
    print os.getcwd()
    for index in range(1,len(arguments)):
        arguments[index] = arguments[index].encode("ascii")
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
        , 'bday': "chkbday"
        , 'ip': "send-ip"
        , '3ed': "play-3ed"
        , 'at': "make-at"
        , 'atme': "make-atme"
    }.get(message, "pberr")

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
    subprocess.Popen(sub \
    , preexec_fn=chuser(pw_record.pw_uid, pw_record.pw_gid),env=env)  
  
def speakHelper(msg, repeat):
    msgToSpeakFile = codecs.open('/data/archbkp/robot/voice/msg.js','w','utf-8')
    msgToSpeak = msg
    if repeat == 'speakr':    #speakr = speak + repeat
        msgToSpeak = msgToSpeak +unicode('، أُكَرِّر ،','utf-8')+ msg 
    msgToSpeakFile.write('var message = '+ msgQuote(msgToSpeak))
    subProcess('robo-speak')

def msgQuote(msg):
    return '\"' + msg + '\"'