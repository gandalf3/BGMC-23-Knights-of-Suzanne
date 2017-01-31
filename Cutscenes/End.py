import bge
from utils import switchlevel
from Cutscene import Cutscene

def objs(name):
    return bge.logic.getCurrentScene().objects[name]
    
script = Cutscene()

@script.register_event(0)
def do():
    objs("Player").player_control = False

@script.register_event(1)
def do():
    objs("Player").look((-1, 0, 0))
    
@script.register_event(1)
def do():
    objs("Frank").goto(objs("Empty.003").worldPosition.copy())
    objs("Frank").look((1,0,0))

@script.register_event(3, pause=True)
def do():
    objs("Frank").say("What's that?", persist=True)

@script.register_event(4, pause=True)
def do():
    objs("Frank").say("You are looking for the next level?", persist=True)
    
@script.register_event(5, pause=True)
def do():
    objs("Frank").say("Well, the programmer has to submit this in 10 minutes", persist=True)
    
@script.register_event(7, pause=True)
def do():
    objs("Frank").say("They told me to tell you.. Sorry.", persist=True)

@script.register_event(10, pause=True)
def do():
    objs("Frank").say("...", persist=True)

@script.register_event(11, pause=True)
def do():
    objs("Frank").say("At any rate, you should be congratulated for persevering through that forest!", persist=True)
    
@script.register_event(13, pause=True)
def do():
    objs("Frank").say("Now... to be continued?", persist=True)

@script.register_event(14)
def do():
    objs("Frank").textbox.fade = 0
    
@script.register_event(16)
def do():
    switchlevel("Suzton")