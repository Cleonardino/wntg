import tkinter as tk
from world.constants import *
from world.screen import ScreenManager
from world.location import FirstScreen, Location, lc_points, connections
from world.player import Player
from world.event_ribbon import EventRibbon
from world.dataloader import possible_keys

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("WNTGP")
        self.geometry("{width}x{height}".format(width=WINDOW_WIDTH,height=WINDOW_HEIGHT))
        self.configure(bg=BG_COLOR)
        self.manager = ScreenManager(self)
        self.event_ribbon : EventRibbon = EventRibbon(self, displayed_count=3)
        self.player : Player = Player(possible_keys)
        
        self.manager.register("first", FirstScreen(self, self.manager, self.player, self.event_ribbon))
        self.manager.register("second", Location(self, self.manager, "start", lc_points, connections, self.player, self.event_ribbon))
        
        self.manager.show("first")
        self.manager.add_overlay(self.event_ribbon)


if __name__ == "__main__":
    app = App()
    app.mainloop()