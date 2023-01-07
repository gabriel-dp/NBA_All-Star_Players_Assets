# python <program>.py <file_path>.json '<url>'

import argparse
from pathlib import Path
import json
import requests

parser = argparse.ArgumentParser()
parser.add_argument("path", type=Path)
parser.add_argument("url", type=str)

arg_path = parser.parse_args().path
arg_url = parser.parse_args().url

json_file = open(arg_path)
data = json.load(json_file)

for element in data['data']:
    response = requests.post(arg_url, json=element)
    print(response)