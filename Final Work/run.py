#!/usr/bin/env python3

import os
import requests

local_folder = 'supplier-data/descriptions/'
url = 'http://35.202.16.26/fruits/'

for filename in os.listdir(local_folder):
    if '.txt' in filename:
        filepath = os.path.join(local_folder, filename)
        data = {}
        with open(filepath, 'r') as f:
            data['name'] = f.readline()
            data['weight'] = int(f.readline().split(' lbs')[0])
            data['description'] = f.readline()
            data['image_name'] = filename.replace('txt', 'jpeg')

        request = requests.post(url=url, json=data)
