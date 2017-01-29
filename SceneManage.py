import bge
from Cutscenes import *
from utils import getScene
import Accomplishments

cutscenes = {\
"hi_frank": HiFrank,
"castle_lawn_meeting": CastleLawn,
}

def cont_switchlevel(cont):
    own = cont.owner
    bge.logic.getCurrentScene().replace(own["toscene"])
    
def run_cutscene(name):
    bge.logic.getCurrentScene().objects["Control"]['running_cutscene'] = name
    
def cont_cutscene(cont):
    own = cont.owner
    run_cutscene(own["cutscene"])

def fade_out(cont):
    own = cont.owner
    
    own.color[3] -= .01
    if own.color[3] <= 0:
        own.visible = False
    

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