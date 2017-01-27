import bge

class Typewriter(bge.types.KX_FontObject):
    def __init__(self, own):
        self.line = "" # message to be typed out
        self.speed = 1 #chars per tic
        self.caret_pos = 0 # position of typing cursor thingy
        
    def onEOL(self):
        pass
    
    def typewrite(self):
        if self.caret_pos <= len(self.line):
            self.text = self.line[0:self.caret_pos]
            self.caret_pos += 1
        
class Dialog(Typewriter):
    def __init__(self, own):
        Typewriter.__init__(self, own)
    
    def write(self, str):
        self.line = str
        self.caret_pos = 0
        
    def align_to_camera(self):
        cam = bge.logic.getCurrentScene().active_camera
        camera_vec = cam.worldPosition - self.worldPosition
        
        self.alignAxisToVect((0,0,1), 1, 1)
        self.alignAxisToVect(camera_vec, 2, .2)
        
    def adjust_position(self):
        tpos = self.target_pos.copy()
        tpos.z += .3
        tpos.x -= 1
        self.worldPosition = self.worldPosition.lerp(tpos, .1)
        
    def main(self):
        self.typewrite()
        self.align_to_camera()
        self.adjust_position()
    
        
def run_dialog(cont):
    own = cont.owner
    
    if "typer_init" not in own:
        own["typer_init"] = True
        #own = Dialog(own)
    
    own.main()
        
        
def increment(object):
    i = int(object.text)
    print("increment", i)
    object.text = str(i+1)
    
    
    