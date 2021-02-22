#!/usr/bin/env python3

import datetime
import os
import reports
import emails

paragraph = []
attachment = '/tmp/processed.pdf'
title = 'Processed Update on {}'.format(datetime.datetime.today().strftime('%B  %d, %Y'))
local_folder = 'supplier-data/descriptions/'
for filename in os.listdir(local_folder):
    if '.txt' in filename:
        filepath = os.path.join(local_folder, filename)
        data = {}
        temp = []
        with open(filepath, 'r') as f:
            data['name'] = f.readline().strip()
            data['weight'] = f.readline().strip()
        temp = ['name: {} <br/> weight: {}'.format(data['name'], data['weight'])]
        paragraph.append(temp)

if __name__ == "__main__":
    reports.generate_report(attachment, title, paragraph)
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
    message = emails.generate_email(sender, receiver, subject, body, attachment)
    emails.send_email(message)
