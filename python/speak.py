#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import subprocess
import os
import sys
import pwd  
import signal
import codecs

  
def speakHelper(msg, repeat):
    msgToSpeakFile = codecs.open('/data/archbkp/robot/voice/msg.js','w','utf-8')
    msgToSpeak = msg
    if repeat == 'speakr':    #speakr = speak + repeat
        msgToSpeak = msgToSpeak +unicode('، أُكَرِّر ،','utf-8')+ msg 
    msgToSpeakFile.write('var message = '+ msgQuote(msgToSpeak))
    subProcess('robo-speak')


def subProcess(sub):
    subprocess.Popen(sub, shell=True \
    , preexec_fn=chuser(pw_record.pw_uid, pw_record.pw_gid),env=env)  
  


def msgQuote(msg):
    return '\"' + msg + '\"'