#!/usr/local/bin/python3

import os
import requests

keys = ["title", "name", "date", "feedback"]
d = {}

feedback = os.listdir("/data/feedback")
for file in feedback:
  with open("/data/feedback/" + file) as entry:
    i = 0
    for line in entry:
      d[keys[i]] = line
      i = i + 1
  print(d)
  requests.post("http://34.168.158.242/feedback/", data=d)