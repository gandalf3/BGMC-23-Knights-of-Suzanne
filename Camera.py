import bge


def main(cont):
    own = cont.owner
    focus = bge.logic.getCurrentScene().objects[own["focus"]]
    
    own.worldPosition.x = own.worldPosition.lerp(focus.worldPosition, .1).x