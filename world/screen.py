import tkinter as tk
from world.constants import *
from world.player import Player
from world.event_ribbon import EventRibbon

class ScreenManager:
    """Owns one instance per registered screen and swaps which frame is
    visible. Screens are never destroyed — just hidden/shown — so their
    internal state (and the widgets themselves) persist across visits.
    Also update the owned_keys if possible"""

    def __init__(self, root):
        self.root = root
        self.overlays : list[tk.Widget] = [] # List of widget to keep in front
        self.screens : dict[str, Screen] = {}  # name -> Screen instance
        self.current_screen : Screen = None
        self.desc_button : tk.Button = None

    def register(self, name, screen):
        self.screens[name] = screen
    
    def add_overlay(self, overlay : tk.Widget):
        self.overlays.append(overlay)

    def show(self, name):
        if name not in self.screens:
            raise ValueError(f"Screen '{name}' not found in registry")

        if self.current_screen is not None:
            self.current_screen.get_frame().place_forget()

        screen = self.screens[name]
        screen.get_frame().place(x=0, y=0, relwidth=1, relheight=1)
        self.current_screen = screen
        for overlay in self.overlays:
            overlay.tkraise()
    
    def show_description(self, text : str):
        """Show an exploration description
        """
        self.desc_button = tk.Button(
            self.root,
            anchor='center',
            text=text,
            fg= FG_COLOR,
            bg=BG_COLOR,
            font=FONT,
            command=self.remove_description
        )
        self.desc_button.pack(side="top", pady=100, anchor="center")
        self.current_screen.reset_state(False)
        
        
    def remove_description(self):
        self.desc_button.pack_forget()
        self.desc_button = None
        self.current_screen.reset_state(True)

class Screen:
    """Base class for a screen. NOT a tk.Frame itself — instead, build()
    constructs and returns a tk.Frame. The frame is built once (lazily)
    and cached, so it is never destroyed; navigating away just hides it
    with place_forget(), and navigating back shows it again with the
    same widgets and state intact.

    Subclasses override build() to construct their own frame/widgets.
    """

    def __init__(self, master, manager, player : Player, event_ribbon : EventRibbon):
        self.master = master
        self.manager : ScreenManager = manager
        self.frame = None  # created lazily on first show
        self.player : Player = player
        self.event_ribbon : EventRibbon = event_ribbon

    def get_frame(self) -> tk.Widget:
        """Return this screen's frame, building it on first access."""
        if self.frame is None:
            self.frame = self.build()
        return self.frame

    def build(self):
        """Override in subclasses. Must create and return a tk.Frame
        (with self.master as its parent) containing the screen's widgets."""
        raise NotImplementedError

    # --- Helpers available to subclasses ---

    def make_label(self, parent, text, x, y):
        label = tk.Label(parent, text=text, bg=BG_COLOR, fg=FG_COLOR, font=FONT)
        label.place(x=x, y=y)
        return label

    def make_button(self, parent, text, x, y, command):
        border = tk.Frame(parent, bg=FG_COLOR, padx=2, pady=2)
        border.place(x=x, y=y)

        button = tk.Button(
            border,
            text=text,
            command=command,
            bg=BG_COLOR,
            fg=FG_COLOR,
            activebackground=BG_COLOR,
            activeforeground=FG_COLOR,
            font=FONT,
            relief=tk.FLAT,
            borderwidth=0,
            padx=20,
            pady=10,
        )
        button.pack()
        return button
    
    def reset_state(activated : bool) -> None:
        """Override in subclasses. Must make the screen activated or not,
        along with all its widgets. Reset all widget to the desired state."""
        raise NotImplementedError