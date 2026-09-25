import json
from world.constants import *

with open(KEYS_PATH, 'r') as keys_file:
    possible_keys = json.load(keys_file)