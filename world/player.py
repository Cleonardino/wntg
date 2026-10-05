from world.constants import *

class Player:
    def __init__(
        self,
        master,
        possible_keys : dict[str, dict],
        owned_keys : set[str] = set()
		):
        
        self.book : Book = Book(
            master=master,
            possible_keys=possible_keys,
            owned_keys=owned_keys
        )
    
    def get_book(self):
        return self.book
        
    
    

class Book():
    """Represent the database that the player have"""
    def __init__(self,
                 master,
                 possible_keys : dict[str, dict],
                 owned_keys : set[str]):

        super().__init__()
        self.master = master
        self.possible_keys : dict[str, dict] = possible_keys.copy()
        self.owned_keys : set[str] = owned_keys.copy()
    
    def tkraise(self):
        # TODO
        # for label in self.labels:
        #     label.tkraise()
        pass
    
    def get_owned_keys(self):
        return self.owned_keys
    
    def has_key(self, id : str):
        return id in self.owned_keys
    
    # Try to add the key, return if key was successfully added. Key is not added if already present
    def add_key(self, id : str) -> bool:
        if self.has_key(id):
            return False
        self.owned_keys.add(id)
        return True
    
    def get_key_name(self, id : str) -> bool:
        return self.possible_keys[id]["name"]