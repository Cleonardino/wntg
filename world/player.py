from world.constants import *

class Player:
    def __init__(
		self,
		possible_keys : dict[str, dict],
		owned_keys : dict[str] = {}
		):
        self.possible_keys = possible_keys.copy()
        self.owned_keys = owned_keys.copy()
    
    def has_key(self, id : str):
        return id in self.owned_keys
    
    # Try to add the key, return if key was successfully added. Key is not added if already present
    def add_key(self, id : str) -> bool:
        if self.has_key(id):
            return False
        self.owned_keys[id] = True
        return True
    
    def get_key_name(self, id : str) -> bool:
        return self.possible_keys[id]["name"]