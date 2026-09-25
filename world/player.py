from world.constants import *

class Player:
    def __init__(
		self,
		possible_keys : dict[str, dict],
		owned_keys : dict[str] = {}
		):
        self.possible_keys = possible_keys.copy()
        self.owned_keys = owned_keys.copy()
    
    def has_key(self, name : str):
        return name in self.owned_keys
    
    # Try to add the key, return if key was successfully added. Key is not added if already present
    def add_key(self, name : str) -> bool:
        if name in self.owned_keys.keys():
            return False
        self.owned_keys[name] = True
        return True

possibles = {
	"secret1" : {
		"name" : "A true secret",
		"type" : "explore"
	},
    "secret2" : {
		"name" : "Another true secret",
  		"type" : "knowledge",
		"desc" : "The secret is that you can in fact click on the button !",
		"color" : PLAYER_COLOR
	}
}

player = Player(
	possibles,

)