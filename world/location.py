from world.screen import Screen
from world.constants import *
from world.player import Player
from world.event_ribbon import EventRibbon
import tkinter as tk

class LocationPoint():
    """A point inside a vaste location.
    \nexploration is the text displayed when exploring.
    \nName of location point is its key in location (not in this class).
    \ngiven_key is key name given when exploring.
    \nrequired_key is key required to access this points
    \n 
    """
    def __init__(
        self,
        exploration : str,
        x : int,
        y : int,
        given_key : str = "",
        ):
        self.exploration : str = exploration
        self.x = x
        self.y = y
        self.given_key = given_key
        self.button : tk.Button = None

class Location(Screen):
    def __init__(
        self,
        master,
        manager,
        start : str,
        location_points : dict[str, LocationPoint],
        connections : list[tuple[str]],
        player : Player,
        event_ribbon : EventRibbon
        ):
        super().__init__(master=master, manager=manager, player=player, event_ribbon=event_ribbon)
        self.current_point : str = start
        self.location_points : dict[str, LocationPoint] = location_points
        self.canvas : tk.Canvas = None
        self.connections : list[Connection] = connections
    
    def update_location(self):
        # Updating accessible location points
        self.location_points[self.current_point].button.config(state=tk.NORMAL)
        for cur_name in self.location_points:
            self.location_points[cur_name].button.config(state=tk.DISABLED)
        for connection in self.connections:
            point_a : str = connection.point_a
            point_b : str = connection.point_b
            if ((point_a == self.current_point or point_b == self.current_point) and
                not connection.is_blocked(self.player.owned_keys)
                ):
                # We need : from starting point, accessible if next to it, and 
                # if hidden, player have viewing key and if a key is also required player have it
                self.location_points[point_a].button.config(state=tk.NORMAL)
                self.location_points[point_b].button.config(state=tk.NORMAL)
        
        self.update_canvas()
    
    def update_canvas(self):
        self.canvas.delete("all")
        
        # Draw character
        self.canvas.create_oval(
            self.location_points[self.current_point].x + PLAYER_OFFSET[0],
            self.location_points[self.current_point].y + PLAYER_OFFSET[1],
            self.location_points[self.current_point].x + PLAYER_OFFSET[0] + PLAYER_SIZE[0],
            self.location_points[self.current_point].y + PLAYER_OFFSET[1] + PLAYER_SIZE[1],
            fill=PLAYER_COLOR
        )
        
        # Draw connections
        for connection in self.connections:
            point_a : str = connection.point_a
            point_b : str = connection.point_b
            self.canvas.create_line(
                self.location_points[point_a].x + 20,
                self.location_points[point_a].y + 20,
                self.location_points[point_b].x + 20,
                self.location_points[point_b].y + 20,
                fill=FG_COLOR
            )
    
    def build(self):
        frame = tk.Frame(self.master, bg=BG_COLOR)
        self.canvas = tk.Canvas(frame,background=BG_COLOR,width=WINDOW_WIDTH,height=WINDOW_HEIGHT)
        self.canvas.place(x=0,y=0)
        
        for cur_name in self.location_points:
            self.location_points[cur_name].button = self.make_button(
                frame,
                cur_name,
                self.location_points[cur_name].x,
                self.location_points[cur_name].y,
                lambda name=cur_name: self.go_to(name)
            )
           
        self.update_location()
        
        return frame
    
    def reset_state(self, activated):
        if activated:
            self.update_location()
        else:
            for cur_name in self.location_points:
                self.location_points[cur_name].button.config(state=tk.DISABLED)
    
    def go_to(self, destination : str):
        if destination == self.current_point:
            # Going to current point, exploring
            print("exploring " + destination)
            self.manager.show_description(self.location_points[destination].exploration)
            to_give : str = self.location_points[destination].given_key
            if to_give:
                if self.player.add_key(to_give):
                    print("given key: " + to_give)
                    self.event_ribbon.register_message("You found " + self.player.get_key_name(to_give))
            return
        
        print("going to " + destination)
        
        # Moving
        self.current_point = destination
        
        self.update_location()
        
class Connection():
    def __init__(
        self,
        point_a : str,
        point_b : str,
        required_key : str = "",
        viewing_key : str = ""
        ):
        self.point_a : str = point_a
        self.point_b : str = point_b
        self.required_key : str = required_key
        self.viewing_key : str = viewing_key
    
    def is_blocked(self, owned_keys : dict[str]):
        return (
            (self.viewing_key != "" and not self.viewing_key in owned_keys) or
            (self.required_key != "" and not self.required_key in owned_keys)
            )
        
class FirstScreen(Screen):
    def build(self):
        frame = tk.Frame(self.master, bg=BG_COLOR)
        self.make_label(frame, "This is the first screen.", 350, 300)
        self.make_button(frame, "Go to second screen", 380, 400, self.go_next)
        return frame

    def reset_state(activated):
        pass
    
    def go_next(self):
        self.manager.show("second")

lc_points : dict[str, LocationPoint] = {
    "start": LocationPoint(
        "You explored start\nIt is, well... a good start I think\nThis text is really long on purpose as a matter of testing",
        10,
        10
    ),
    "mystery": LocationPoint(
        "Hello",
        500,
        500,
        given_key="secret1"
    ),
    "mystery2": LocationPoint(
        "Hello",
        500,
        600,
        given_key="secret2"
    ),
    "secret": LocationPoint(
        "Hello",
        10,
        100,
    ),
    "blocked": LocationPoint(
        "Hello",
        200,
        10,
    )
}

connections : list[Connection] = [
    Connection("start","mystery"),
    Connection("mystery2","mystery"),
    Connection("start","blocked",required_key="secret1"),
    Connection("start","secret",viewing_key="secret2")
]