import shutil
import os

source_dir = 'templates'
dest_dir = '.'

files = os.listdir(source_dir)

for file in files:
    if file.endswith('.html'):
        shutil.copy(os.path.join(source_dir, file), dest_dir)