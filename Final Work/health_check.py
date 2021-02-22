#!/usr/bin/env python3
import os
import shutil
import psutil
from time import sleep
import socket
import emails


while True:
    error = 0
    cpu_load = psutil.cpu_percent(interval=1)
    total, used, free = shutil.disk_usage(__file__)
    mem = psutil.virtual_memory()
    THRESHOLD = 500 * 1024 * 1024  # 500MB
    try:
        address = socket.gethostbyname('localhost')
    except:
        address = ''
    if cpu_load > 80:
        subject = "Error - CPU usage is over 80%"
        error = 1
    elif free / total < 0.2:
        subject = "Error - Available disk space is less than 20%"
        error = 1
    elif mem.available <= THRESHOLD:
        subject = "Error - Available memory is less than 500MB"
        error = 1
    elif address != "127.0.0.1":
            subject = "Error - localhost cannot be resolved to 127.0.0.1"
            error = 1
    if error == 1:
        sender = "automation@example.com"
        receiver = "{}@example.com".format(os.environ.get('USER'))
        body = 'Please check your system and resolve the issue as soon as possible.'
        message = emails.generate_email(sender, receiver, subject, body, None)
        emails.send_email(message)
    sleep(60)
