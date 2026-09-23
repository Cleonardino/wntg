from world.constants import *
import tkinter as tk


class EventRibbon():
    def __init__(self, master, displayed_count : int = 10):
        super().__init__()
        self.master = master
        self.frame = tk.Frame(self.master, bg=BG_COLOR)
        self.labels = []
        for i in range(displayed_count):
            cur_label = tk.Label(self.frame,text="test",fg="white",bg="red")
            cur_label.place(x=0,y=EVENT_RIBBON_ELEM_HEIGHT * i)
            self.labels.append(cur_label)
    
    def get_frame(self):
        return self.frame
    
    def register_message(self, message : str, color : str):
        pass