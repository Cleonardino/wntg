import json
import os
from world.constants import *

with open(KEYS_PATH, 'r') as keys_file:
    possible_keys = json.load(keys_file)

locations_dict : dict = {}
for filename in os.listdir(LOCATIONS_DIR_PATH):
	file_path = os.path.join(LOCATIONS_DIR_PATH, filename)
	if os.path.isfile(file_path):
		with open(file_path, 'r') as location_file:
			locations_dict[filename.split(".")[0]] = json.load(location_file)