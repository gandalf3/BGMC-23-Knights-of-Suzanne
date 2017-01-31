import bge
from Cutscene import Cutscene

def objs(name):
    return bge.logic.getCurrentScene().objects[name]
script = Cutscene()

@script.register_event(0)
def do():
    objs("Player").player_control = False
    
@script.register_event(1)
def do():
    objs("Ton_of_Ideas").look((0, 1, 0))

@script.register_event(1)
def do():
    objs("Frank").goto(objs("Frankholder.003").worldPosition)

@script.register_event(1)
def do():
    objs("Player").goto(objs("Frankholder.002").worldPosition)

@script.register_event(6)
def do():
    objs("Player").look((0,1,0))

@script.register_event(7, pause=True)
def do():
    objs("Ton_of_Ideas").say("...")

@script.register_event(7.5, pause=True)
def do():
    objs("Ton_of_Ideas").say("Terrible, isn't it?", persist=True)
    
@script.register_event(8)
def do():
    objs("Ton_of_Ideas").look((-1,0,0))
    
@script.register_event(8)
def do():
    objs("Ton_of_Ideas").say("!")
    
@script.register_event(8.5)
def do():
    objs("Player").look((1,0,0))
    
@script.register_event(9, pause=True)
def do():
    objs("Ton_of_Ideas").say("Your eyes.. Something about them seems familiar", persist=True)
    
@script.register_event(9.5, pause=True)
def do():
    objs("Ton_of_Ideas").say("Could it be..?", persist=True)
    
@script.register_event(10, pause=True)
def do():
    objs("Ton_of_Ideas").say("They remind me of Cycles the Magnificent", persist=True)
    
@script.register_event(11, pause=True)
def do():
    objs("Ton_of_Ideas").say("You have the light of a Path Tracer within you", persist=True)

@script.register_event(12)
def do():
    objs("Ton_of_Ideas").say("Here", persist=True)
    
@script.register_event(12.8, pause=True)
def do():
    objs("Ton_of_Ideas").say("Take the Sword of Twin Polygons", persist=True)
    objs("Player").children["PlayerVisual"].children["Sword"].visible = True
    
@script.register_event(13, pause=True)
def do():
    objs("Ton_of_Ideas").say("That belonged to Cycles", persist=True)
    
@script.register_event(14)
def do():
    objs("Ton_of_Ideas").say("!")
    objs("Player").look((-1,0,0))
    objs("Frank").look((-1,0,0))

@script.register_event(14)
def do():
    objs("Sir_Sergey").goto(objs("Frankholder.004").worldPosition)
    objs("Sir_Blendsalot").goto(objs("Frankholder.005").worldPosition)
    objs("Sir_Sergey").look((1, 0, 0))
    objs("Sir_Blendsalot").look((1, 0, 0))
    
@script.register_event(19)
def do():
    objs("Sir_Blendsalot").say("Teapotists!")
    objs("Sir_Sergey").look((1, 0, 0))
    objs("Sir_Blendsalot").look((1, 0, 0))
    
@script.register_event(3+18, pause=True)
def do():
    objs("Sir_Blendsalot").say("There were Tons of them, blowing steam everywhere")
    
@script.register_event(3+19, pause=True)
def do():
    objs("Sir_Blendsalot").say("... no pun intended")
    
@script.register_event(3+20, pause=True)
def do():
    objs("Ton_of_Ideas").say("...", persist=True)
    
@script.register_event(3+20.5, pause=True)
def do():
    objs("Sir_Sergey").say("It seems likely they took the 2.8")
    
@script.register_event(3+21)
def do():
    objs("Ton_of_Ideas").say("Well then, the way is clear", persist=True)
    
@script.register_event(3+23, pause=True)
def do():
    objs("Ton_of_Ideas").say("The holder of the Sword of Twin Polygons must find a path", persist=True)
    
@script.register_event(3+23.5, pause=True)
def do():
    objs("Ton_of_Ideas").textbox.fade = 0
    objs("Sir_Blendsalot").say("He gave you the Twin Polygons?", persist=True)
    
@script.register_event(3+24)
def do():
    objs("Sir_Blendsalot").say("Well, I won't judge.", persist=True)
    
@script.register_event(3+25, pause=True)
def do():
    objs("Sir_Blendsalot").say("They went into the Particulous Forest", persist=True)
    
@script.register_event(3+26)
def do():
    objs("Sir_Blendsalot").say("Good luck!")

@script.register_event(3+27)
def do():
    bge.logic.globalDict["accomplishments"]["sword"] = True
    objs("Player").player_control = True
