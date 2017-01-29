import bge
from utils import getScene, switchlevel
from Typewriter import Dialog
from Cutscene import Cutscene

def objs(name):
    return bge.logic.getCurrentScene().objects[name]
script = Cutscene()

villagers = ['Scales', 'Anne', 'Suzie', 'Sue', 'Alice', 'Kewler', 'Zane', 'Frank']

@script.register_event(0)
def do():
    objs("Camera")["focus"] = "Sir_Sergey"
    
@script.register_event(0)
def do():
    objs("Player").player_control = False

@script.register_event(0)
def do():
    objs("Player").goto(objs("Playerholder").worldPosition.copy())

@script.register_event(0)
def do():
    objs("Player").lookat(objs("Sir_Sergey"))

@script.register_event(1)
def do():
    objs("Alice").say("Golly")
    
@script.register_event(1.5)
def do():
    objs("Anne").say("Gee")
    
@script.register_event(2)
def do():
    objs("Kewler").say("What happened?")
    
@script.register_event(2.3)
def do():
    objs("Suzie").say("Yeah, what's going on?")

@script.register_event(2.8)
def do():
    objs("Sir_Sergey").draw_attention()
    
@script.register_event(3)
def do():
    objs("Sir_Sergey").say("Quiet please!", emphasis=True, persist=True)

@script.register_event(3.2, pause=True)
def do():
    for o in [bge.logic.getCurrentScene().objects[n] for n in villagers]:
        try:
            o.textbox.fade=0
        except AttributeError:
            print(o.name, "has no valid textbox")

@script.register_event(4)
def do():
    objs("Sir_Sergey").say("Someone has just made off with the 2.8!", persist=True)

@script.register_event(5)
def do():
    for o in [bge.logic.getCurrentScene().objects[n] for n in villagers]:
        o.draw_attention()

@script.register_event(5)
def do():
    collective = objs("Villagers")
    tscn = getScene("TextOverlay")
    gasp = Dialog(tscn.addObject("GenericDialog", collective))
    gasp.target_pos = collective.worldPosition
    gasp.localScale *= 3
    gasp.write("*GASP*")
    gasp.fade = 2
    
@script.register_event(5.6)
def do():
    objs("Kewler").say("WHAT!")
    
@script.register_event(6)
def do():
    objs("Zane").say("Oh no!")

@script.register_event(6.5, pause=True)
def do():
    objs("Sue").say("Who would do such a thing!?", persist=True)

@script.register_event(6.3, pause=True)
def do():
    objs("Frank").say("Did anyone see who did it?", persist=True)

@script.register_event(7.1, pause=True)
def do():
    objs("Scales").say("What are we going to do?", persist=True)
    
@script.register_event(7.5)
def do():
    objs("Sir_Sergey").draw_attention()
    
@script.register_event(8, pause=True)
def do():
    objs("Sir_Sergey").say("Settle down, settle down", persist=True)
    
@script.register_event(8.5)
def do():
    for o in [bge.logic.getCurrentScene().objects[n] for n in villagers]:
        try:
            o.textbox.fade=0
        except AttributeError:
            print(o.name, "has no valid textbox")
    
@script.register_event(9)
def do():
    objs("Sir_Sergey").say("Sir Blendsalot is already after them", persist=True)
    
@script.register_event(11)
def do():
    objs("Sir_Sergey").say("!")
    
@script.register_event(11.5)
def do():
    objs("Sir_Sergey").look((1, 0, 0))
    
@script.register_event(12)
def do():
    objs("Sir_Sergey").say("Why, here he comes now!", persist=True)
    
@script.register_event(12)
def do():
    objs("Sir_Blendsalot").goto(objs("Sir_Sergey").worldPosition.copy())

@script.register_event(12.5, pause=True)
def do():
    objs("Sir_Blendsalot").say("huff.. puff..")
    objs("Sir_Sergey").textbox.fade = 0

@script.register_event(13)
def do():
    objs("Sir_Sergey").say("Well?")

@script.register_event(13.9)
def do():
    objs("Frank").lookat(objs("Player"))

@script.register_event(14, pause=True)
def do():
    objs("Frank").say("The 2.8 missing.. After the time the Council put into it..", persist=True)
    
@script.register_event(14.3)
def do():
    objs("Sir_Blendsalot").say("...")
    
@script.register_event(14.8)
def do():
    objs("Sir_Sergey").say("...")

@script.register_event(15, pause=True)
def do():
    objs("Frank").say("I mean, it's hard to believe.. Lets go see", persist=True)
    
@script.register_event(15.2)
def do():
    objs("Frank").goto(objs("Frankholder.001").worldPosition.copy())
    
@script.register_event(16)
def do():
    switchlevel("Castle")
