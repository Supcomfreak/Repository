#!/usr/bin/python
import datetime
from subprocess import call
title = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")+".png"
call(["import", title])

