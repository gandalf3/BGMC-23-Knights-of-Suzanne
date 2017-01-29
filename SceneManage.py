import bge
from Cutscenes import *
from utils import getScene, switchlevel
import Accomplishments
import aud

cutscenes = {\
"hi_frank": HiFrank,
"castle_lawn_meeting": CastleLawn,
"castle_sword": CastleSword,
}

def cont_switchlevel(cont):
    own = cont.owner

    if "tospawn" in own:
        bge.logic.globalDict["next_spawn"] = own["tospawn"]
    if "requirement" in own:
        if bge.logic.globalDict.get(own["requirement"], True):
            switchlevel(own["toscene"])
    else:
        switchlevel(own["toscene"])
    
def run_cutscene(name):
    bge.logic.getCurrentScene().objects["Control"]['running_cutscene'] = name
    
def cont_cutscene(cont):
    own = cont.owner
    run_cutscene(own["cutscene"])

def blackfade(cont):
    own = cont.owner
    if own.get("in"):
        if own.color[3] >= 0:
            own.color[3] -= .01
            if own.color[3] <= 0:
                own.visible = False
    else:
        own.visible = True
        own.color[3] += .01
        if own.color[3] >= 1:
            own["black"] = True
            switchlevel(own.get("next_lvl"))
            stophandles()
            
def stophandles():
    scn = bge.logic.getCurrentScene()
    ctrl = scn.objects["Control"]
    for h in ctrl.get("sounds", []):
        if h.status == aud.AUD_STATUS_PLAYING:
            h.stop()

def main(cont):
    own = cont.owner
    
    if "game_init" not in own:
        own["game_init"] = True
        accomp = bge.logic.globalDict.get("accomplishments", False)
        if not accomp:
            bge.logic.globalDict["accomplishments"] = Accomplishments.accomplishments
            
    
    if "overlay_init" not in own:
        own["overlay_init"] = True
        bge.logic.addScene("TextOverlay", 1)
        
    else:
        if bge.logic.getCurrentScene().name != "TextOverlay":
            scn = getScene("TextOverlay")
            scn.objects["TextOverlayCamera"].worldTransform = bge.logic.getCurrentScene().objects["Camera"].worldTransform
            
            if own.get("running_cutscene", 0):
                cutscenes[own["running_cutscene"]].script.run()