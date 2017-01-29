import bge
import Sound
from utils import clamp

def main(cont):
    own = cont.owner
    focus = bge.logic.getCurrentScene().objects[own["focus"]]
    
    own.worldPosition.x = clamp(own.worldPosition.lerp(focus.worldPosition, .1).x, own.get("xmin", -500), own.get("xmax", 500))
    Sound.update_device(own)