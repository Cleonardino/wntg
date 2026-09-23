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
                text="",
                fg=FG_COLOR,
                bg=BG_COLOR,
                font=FONT
                )
            
            cur_label.place(x=0,y=EVENT_RIBBON_ELEM_HEIGHT * i)
            self.labels.append(cur_label)
    
    def tkraise(self):
        for label in self.labels:
            label.tkraise()
    
    def register_message(self, message : str, color : str = NORMAL_M_COLOR):
        # Push front all messages. first label message (more ancient is not kept)
        for i in range(len(self.labels) - 1):
            self.labels[i].config(text=self.labels[i+1].cget("text"))
            self.labels[i].config(fg=self.labels[i+1].cget("fg"))
        # Set new message
        self.labels[-1].config(text=message)
        self.labels[-1].config(fg=color)