import os
from pathlib import Path
from os import listdir
from os.path import isfile, join

main_path = Path(__file__).parent.parent
logos_folder = 'teams/logo'
new_logos_folder = '_automation/new_files'

src_path = (main_path / logos_folder).resolve()
new_path = (main_path / new_logos_folder).resolve()

files = [f for f in listdir(src_path)]


for index, file in enumerate(files):
    old_name = f'svgviewer-output ({index}).svg'
    os.rename((new_path / old_name).resolve(), (new_path /file).resolve())
    