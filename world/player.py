from world.constants import *
import tkinter as tk
from world.screen import Screen

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
    
    # TODO make book a special overlay

class Book(Screen):
    """Represent the database that the player have"""
    def __init__(self,
                 master,
                 possible_keys : dict[str, dict],
                 owned_keys : set[str]):

        self.master = master
        self.possible_keys : dict[str, dict] = possible_keys.copy()
        self.owned_keys : set[str] = owned_keys.copy()
        self.widgets : dict[str, tuple[tk.Frame, tk.Button]] = {}
    
    def build(self):
        self.make_button(self.frame, "Return", WINDOW_WIDTH // 2, 450, self.manager.set_book_state(False))
        return self.frame
    
    def get_owned_keys(self):
        return self.owned_keys
    
    def has_key(self, id : str):
        return id in self.owned_keys
    
    # Try to add the key, return if key was successfully added. Key is not added if already present
    def add_key(self, id : str) -> bool:
        if self.has_key(id):
            return False
        self.owned_keys.add(id)
        frame = tk.Frame(self.master, bg=FG_COLOR, padx=2, pady=2)
        # The id field of possible keys is the index which must be used
        frame.place(x=WINDOW_WIDTH * 0.9,
                     y=BOOK_ELEM_HEIGHT * self.possible_keys[id]["id"] + 25,
                     anchor="center")

        button = tk.Button(
            frame,
            text=id,
            fg=FG_COLOR,
            bg=BG_COLOR,
            font=FONT
            )
        button.pack(anchor="center")
        
        self.widgets[id] = (frame, button)

        return True
    
    def get_key_name(self, id : str) -> bool:
        return self.possible_keys[id]["name"]