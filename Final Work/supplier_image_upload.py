#!/usr/bin/env python3

import os
import requests

local_folder = 'supplier-data/images/'
url = 'http://35.202.16.26/upload/'
for filename in os.listdir(local_folder):
    if '.jpeg' in filename:
        filepath = os.path.join(local_folder, filename)
        with open(filepath, 'rb') as opened:
            request = requests.post(url=url, files={'file': opened})
			