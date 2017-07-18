#!/usr/bin/python
import datetime

#requests will be used when the screenshots are uploaded to a file server automatically
#import requests

from subprocess import call
title = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")+".png"
call(["import", title])
call(["xclip", "-selection", "clipboard", "-t", "image/png", title])
