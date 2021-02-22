#!/usr/bin/env python3

import os
from PIL import Image

local_folder = 'supplier-data/images/'
target_folder = 'supplier-data/images/'
for filename in os.listdir(local_folder):
    filepath = os.path.join(local_folder, filename)
    new_filepath = os.path.join(target_folder, filename.split('.')[0] + '.jpeg')
    try:
        im = Image.open(filepath)
        im.convert('RGB').resize((600, 400)).save(new_filepath)
    except:
        print('File {} cannot be processed'.format(new_filepath))
