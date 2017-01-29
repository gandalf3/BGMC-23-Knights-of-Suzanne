import bge
from Cutscene import Cutscene

objs = bge.logic.getCurrentScene().objects
script = Cutscene()

@script.register_event(0)
def do():
    objs["Player"].player_control = False

@script.register_event(1)
def do():
    objs["Frank"].look((1,0,0))

@script.register_event(2)
def do():
    objs["Frank"].goto(objs["Player"].worldPosition.copy())

@script.register_event(2+.5)
def do():
    objs["Frank"].draw_attention()

@script.register_event(2+.3)
def do():
    objs["Player"].lookat(objs["Frank"])

@script.register_event(2+.6, pause=True)
def do():
    objs["Frank"].say("There you are!", persist=True)
    
@script.register_event(3+1.5, pause=True)
def do():
    objs["Frank"].say("Something's happening down at the castle!", persist=True)

@script.register_event(3+3, pause=True)
def do():
    objs["Frank"].say("Come on, or we'll miss all the excitement!!")
    
@script.register_event(3+4.5)
def do():
    objs["Frank"].goto(objs["Frankholder"].worldPosition.copy())
    
@script.register_event(3+6)
def do():
    objs["Player"].player_control = True
