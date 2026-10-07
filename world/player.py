from world.constants import *
import tkinter as tk

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
        self.buttons : dict[str, tk.Button] = {}
    
    def tkraise(self):
        for button in self.buttons:
            button.tkraise()
    
    def get_owned_keys(self):
        return self.owned_keys
    
    def has_key(self, id : str):
        return id in self.owned_keys
    
    # Try to add the key, return if key was successfully added. Key is not added if already present
    def add_key(self, id : str) -> bool:
        if self.has_key(id):
            return False
        self.owned_keys.add(id)
        border = tk.Frame(self.master, bg=FG_COLOR, padx=2, pady=2)
        border.place(x=WINDOW_WIDTH, y=BOOK_ELEM_HEIGHT,anchor="center")

        self.buttons[id] = tk.Button(
            self.master,
            text=id,
            fg=FG_COLOR,
            bg=BG_COLOR,
            font=FONT
            )
        self.buttons[id].pack()
        return True
    
    def get_key_name(self, id : str) -> bool:
        return self.possible_keys[id]["name"]