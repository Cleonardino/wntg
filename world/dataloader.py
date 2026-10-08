import json
import os
from world.constants import *

with open(KEYS_PATH, 'r') as keys_file:
    # Construct the final key table. It is the same as in the file, except it is a dictionnary
    # with the key being the previous id field and the id field containing the index, used for positionning
    unhashed_possible_keys : list[dict] = json.load(keys_file)
    possible_keys : dict[str, dict]
    for index, element in enumerate(unhashed_possible_keys):
        updated_element = element.copy()
        updated_element["id"] = index
        possible_keys[element["id"]] = updated_element
    

locations_dict : dict = {}
for filename in os.listdir(LOCATIONS_DIR_PATH):
	file_path = os.path.join(LOCATIONS_DIR_PATH, filename)
	if os.path.isfile(file_path):
		with open(file_path, 'r') as location_file:
			locations_dict[filename.split(".")[0]] = json.load(location_file)