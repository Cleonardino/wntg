from world.constants import *
import tkinter as tk


class EventRibbon(tk.Frame):
    def __init__(self, displayed_count : int = 1):
        super().__init__()
        self.frame = tk.Frame(self.master, bg=BG_COLOR)