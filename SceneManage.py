import bge
from Cutscenes import cutscenes
from utils import getScene

def switchlevel(cont):
    own = cont.owner
    bge.logic.getCurrentScene().replace(own["toscene"])
    
def run_cutscene(cont):
    own = cont.owner
    bge.logic.getCurrentScene().objects["Control"]['running_cutscene'] = own["cutscene"]
    

def main(cont):
    own = cont.owner
    
    if "overlay_init" not in own:
        own["overlay_init"] = True
        bge.logic.addScene("TextOverlay", 1)
        
    else:
        if bge.logic.getCurrentScene().name != "TextOverlay":
            scn = getScene("TextOverlay")
            scn.objects["TextOverlayCamera"].worldTransform = bge.logic.getCurrentScene().objects["Camera"].worldTransform
            
            if own.get("running_cutscene", 0):
                cutscenes[own["running_cutscene"]].run()