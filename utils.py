import bge

def getScene(name):
    for s in bge.logic.getSceneList():
        if s.name == "TextOverlay":
            scn = s
    if scn:
        return scn
    else:
        return None