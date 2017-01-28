import bge
from Typewriter import Dialog
from utils import getScene

class CutsceneEvent():
    def __init__(self, time, func):
        self.time = time
        self.func = func
        self.finished = False
        
    def execute(self):
        self.func()

class Cutscene():
    def __init__(self):
        self.events = []
        self.started = False
        
    def register_event(self, time):
        def get_event(func):
            self.events.append(CutsceneEvent(time, func))
            return func
        return get_event
        
        
    def run(self):
        if not self.started:
            self.started = True
            self.t_zero = bge.logic.getRealTime()
            
        now = bge.logic.getRealTime() - self.t_zero
        
        for evt in self.events:
            if not evt.finished and evt.time <= now:
                evt.execute()
                evt.finished = True
        
    

objs = bge.logic.getCurrentScene().objects
castle_lawn = Cutscene()

@castle_lawn.register_event(0)
def do():
    objs["Camera"]["focus"] = "Sir_Sergey"

@castle_lawn.register_event(1)
def do():
    objs["Alice"].say("Golly")
    
@castle_lawn.register_event(1.5)
def do():
    objs["Anne"].say("Gee")
    
@castle_lawn.register_event(2)
def do():
    objs["Kewler"].say("What happened?")
    
@castle_lawn.register_event(2.3)
def do():
    objs["Suzie"].say("Yeah, what's going on?")

@castle_lawn.register_event(2.8)
def do():
    objs["Sir_Sergey"].draw_attention()
    
@castle_lawn.register_event(3)
def do():
    objs["Sir_Sergey"].say("Quiet please!", emphasis=True)

@castle_lawn.register_event(3.2)
def do():
    for o in objs["Villagers"].children:
        if o.textbox:
            o.textbox.fade=0

@castle_lawn.register_event(4)
def do():
    objs["Sir_Sergey"].say("Someone has just made off with the 2.8!")

@castle_lawn.register_event(5)
def do():
    for o in objs["Villagers"].children:
        o.draw_attention()

@castle_lawn.register_event(5)
def do():
    collective = objs["Villagers"]
    tscn = getScene("TextOverlay")
    gasp = Dialog(tscn.addObject("GenericDialog", collective))
    gasp.target_pos = collective.worldPosition
    gasp.localScale *= 3
    gasp.write("*GASP*")
    gasp.fade = 2
    
@castle_lawn.register_event(6)
def do():
    objs["Zane"].say("Oh no!")

@castle_lawn.register_event(6.5)
def do():
    objs["Sue"].say("Who would do such a thing!?")
    
@castle_lawn.register_event(5.6)
def do():
    objs["Kewler"].say("WHAT!")

@castle_lawn.register_event(6.3)
def do():
    objs["Frank"].say("Did anyone see who did it?")

@castle_lawn.register_event(7.1)
def do():
    objs["Scales"].say("What are we going to do?")


cutscenes = {\
"castle_lawn_meeting": castle_lawn,
}