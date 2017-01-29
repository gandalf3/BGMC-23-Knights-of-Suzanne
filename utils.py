import bge
from mathutils import Vector, geometry

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


def clamp(value, min_value=0, max_value=1):
    return max(min(value, max_value), min_value)

class Plane:    
        def __init__(self, vec_p, vec_n,):
            self.p = vec_p
            self.n = vec_n
            
def get_mouse_on_plane(plane, mouse_over):
    ray_p0 = mouse_over.raySource
    ray_p1 = mouse_over.rayTarget
    
    intersection = geometry.intersect_line_plane(ray_p0, ray_p1, plane.p, plane.n)
    return intersection

def switchlevel(name=None):
    scn = bge.logic.getCurrentScene()
    scn.objects["Fadetoblack"]["next_lvl"] = name
    if not scn.objects["Fadetoblack"]["black"]:
        scn.objects["Fadetoblack"]["in"] = False
    else:
        bge.logic.sendMessage("level_shutdown")
        bge.logic.getCurrentScene().replace(name)
    