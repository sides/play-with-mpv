#!/usr/bin/env python

import os
import sys
import json
import struct
import subprocess

def getMessage():
    rawLength = sys.stdin.buffer.read(4)
    if len(rawLength) == 0:
        sys.exit(0)
    messageLength = struct.unpack('@I', rawLength)[0]
    message = sys.stdin.buffer.read(messageLength).decode('utf-8')
    return json.loads(message)

def sendMessage(messageContent):
    encodedContent = json.dumps(messageContent).encode('utf-8')
    encodedLength = struct.pack('@I', len(encodedContent))

    sys.stdout.buffer.write(encodedLength)
    sys.stdout.buffer.write(encodedContent)
    sys.stdout.buffer.flush()

def listen():
    receivedMessage = getMessage()
    subprocess.call(['mpv'] + receivedMessage)
    sendMessage(None)

if __name__ == '__main__':
    listen()
    sys.exit(0)
