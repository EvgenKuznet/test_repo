#!/usr/bin/env python
import signal, time, subprocess

def pidwait(process):
    #signal.signal(signal.SIGKILL, process)
    subprocess.Popen([kill,-0,process])
    output, error = process.communicate()

signal.signal(signal.SIGINT, handler)

subprocess.Popen([,-0,process])
output, error = process.communicate()
pidwait(process)
time.sleep(.1)
