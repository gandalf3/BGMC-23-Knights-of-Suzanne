import bge
from utils import getScene
from Typewriter import Dialog
from Cutscene import Cutscene

objs = bge.logic.getCurrentScene().objects
script = Cutscene()

@script.register_event(0)
def do():
    objs["Camera"]["focus"] = "Sir_Sergey"
    
@script.register_event(0)
def do():
    objs["Player"].player_control = False

@script.register_event(0)
def do():
    objs["Player"].goto(objs["Playerholder"].worldPosition.copy())

@script.register_event(0)
def do():
    objs["Player"].lookat(objs["Sir_Sergey"])

@script.register_event(1)
def do():
    objs["Alice"].say("Golly")
    
@script.register_event(1.5)
def do():
    objs["Anne"].say("Gee")
    
@script.register_event(2)
def do():
    objs["Kewler"].say("What happened?")
    
@script.register_event(2.3)
def do():
    objs["Suzie"].say("Yeah, what's going on?")

@script.register_event(2.8)
def do():
    objs["Sir_Sergey"].draw_attention()
    
@script.register_event(3)
def do():
    objs["Sir_Sergey"].say("Quiet please!", emphasis=True)

@script.register_event(3.2)
def do():
    for o in objs["Villagers"].children:
        if o.textbox:
            o.textbox.fade=0

@script.register_event(4)
def do():
    objs["Sir_Sergey"].say("Someone has just made off with the 2.8!")

@script.register_event(5)
def do():
    for o in objs["Villagers"].children:
        o.draw_attention()

@script.register_event(5)
def do():
    collective = objs["Villagers"]
    tscn = getScene("TextOverlay")
    gasp = Dialog(tscn.addObject("GenericDialog", collective))
    gasp.target_pos = collective.worldPosition
    gasp.localScale *= 3
    gasp.write("*GASP*")
    gasp.fade = 2
    
@script.register_event(5.6)
def do():
    objs["Kewler"].say("WHAT!")
    
@script.register_event(6)
def do():
    objs["Zane"].say("Oh no!")

@script.register_event(6.5)
def do():
    objs["Sue"].say("Who would do such a thing!?")

@script.register_event(6.3)
def do():
    objs["Frank"].say("Did anyone see who did it?")

@script.register_event(7.1)
def do():
    objs["Scales"].say("What are we going to do?")