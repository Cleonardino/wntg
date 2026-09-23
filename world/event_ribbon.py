from world.constants import *
import tkinter as tk


class EventRibbon():
    def __init__(self, master, displayed_count : int = 10):
        super().__init__()
        self.master = master
        self.labels : list[tk.Label] = []
        for i in range(displayed_count):
            cur_label = tk.Label(
                self.master,
                text="test",
                fg="white",
                bg="red",
                font=FONT
                )
            
            cur_label.place(x=0,y=EVENT_RIBBON_ELEM_HEIGHT * i)
            self.labels.append(cur_label)
    
    def tkraise(self):
        for label in self.labels:
            label.tkraise()
    
    def register_message(self, message : str, color : str):
        pass