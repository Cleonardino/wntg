import tkinter as tk
from world.constants import *
from world.screen import ScreenManager, TitleScreen
from world.location import Location, build_locationpoints, build_connections
from world.player import Player
from world.event_ribbon import EventRibbon
from world.dataloader import possible_keys, locations_dict

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("WNTGP")
        self.geometry("{width}x{height}".format(width=WINDOW_WIDTH,height=WINDOW_HEIGHT))
        self.configure(bg=BG_COLOR)
        self.manager = ScreenManager(self)
        self.event_ribbon : EventRibbon = EventRibbon(self, displayed_count=3)
        self.player : Player = Player(self, possible_keys=possible_keys)
        
        self.manager.register("first", TitleScreen(self, self.manager, self.player, self.event_ribbon))
        for packed_location in locations_dict:
            self.manager.register(
                packed_location,
                Location(
                    self,
                    self.manager,
                    locations_dict[packed_location]["start"],
                    build_locationpoints(locations_dict[packed_location]["points"]),
                    build_connections(locations_dict[packed_location]["connections"]),
                    self.player,
                    self.event_ribbon
                    )
                )
        
        self.manager.add_overlay(self.event_ribbon)
        self.manager.add_overlay(self.player.book)
        
        self.manager.show("first")


if __name__ == "__main__":
    app = App()
    app.mainloop()