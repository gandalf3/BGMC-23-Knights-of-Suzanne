import bge

def getScene(name):
    for s in bge.logic.getSceneList():
        if s.name == "TextOverlay":
            scn = s
    if scn:
        return scn
    else:
        return None
    
    
def lerp(value1, value2, fac):
    """
    linear interpolation
    """
    
    return value1 * (1-fac) + value2 * fac