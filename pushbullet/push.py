#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import ConfigParser
import time
import json
import os
import requests
import subprocess
import websocket
import parser


global last_time
global last_message
last_time = time.time()
last_message = ""
def on_error(ws, error):
  print error

def on_close(ws):
  print "closed"

def on_message(ws, message):
  global last_time
  global last_message
  # print time.time()
  # print last_time
  message = json.loads(message)
  if message["type"] == 'nop':
	  return
  deltaTime = time.time() - last_time


  URL = "https://api.pushbullet.com/v2/pushes?modified_after="
  ten_seconds_ago = str(time.time() - 10  * 1000)
  
  data = json.loads(requests.get(URL + ten_seconds_ago, auth=(api_key, '')).content)
  if "title" in data["pushes"][0]:
    theMsg = data["pushes"][0]["title"]
  else:
    theMsg = data["pushes"][0]["body"]
  if deltaTime < 6 and last_message == theMsg:
    return
  theMsg = theMsg.decode('utf8')
  print theMsg
  
    
  parser.parse(theMsg)
  last_message = theMsg
  last_time = time.time()

  print theMsg
#   if message["type"] == "tickle" and message["subtype"] == "push":
#     ten_minutes_ago = str(time.time() - 10 * 60 * 1000)
#     URL = "https://api.pushbullet.com/v2/pushes?modified_after="
#     data = json.loads(requests.get(URL + ten_minutes_ago, auth=(api_key, '')).content)
#     if data["pushes"][0]["title"].strip().lower() in ("start pomodoro", "stop pomodoro"):
#       toggle_donotdisturb()
	
if __name__ == "__main__":
  websocket.enableTrace(True)

  
  apiFile = open('/data/aes/key')
  api_key = apiFile.read().strip()
	
  ws = websocket.WebSocketApp("wss://stream.pushbullet.com/websocket/" + api_key,
							  on_message=on_message,
							  on_error=on_error,
							  on_close=on_close)
	
  ws.run_forever()
