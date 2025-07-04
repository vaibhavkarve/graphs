"""
This type stub file was generated by pyright.
"""

class PlotController:
    normal_mouse_sensitivity = ...
    modified_mouse_sensitivity = ...
    normal_key_sensitivity = ...
    modified_key_sensitivity = ...
    keymap = ...
    def __init__(self, window, *, invert_mouse_zoom=..., **kwargs) -> None:
        ...
    
    def update(self, dt): # -> Literal[True]:
        ...
    
    def get_mouse_sensitivity(self): # -> float:
        ...
    
    def get_key_sensitivity(self): # -> float:
        ...
    
    def on_key_press(self, symbol, modifiers): # -> None:
        ...
    
    def on_key_release(self, symbol, modifiers): # -> None:
        ...
    
    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers): # -> None:
        ...
    
    def on_mouse_scroll(self, x, y, dx, dy): # -> None:
        ...
    
    def is_2D(self): # -> bool:
        ...
    


