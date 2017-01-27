import bge
import Sound


class Typewriter(bge.types.KX_FontObject):
    
    sound_device = Sound.get_device()
    sounds = {\
        "keystroke": Sound.load_factory("click_2.wav", buffer=True).pitch(1.4).volume(.5)
    }
    
    def __init__(self, own):
        self.line = "" # message to be typed out
        self.speed = 1 #chars per tic
        self.caret_pos = 0 # position of typing cursor thingy
        self.resolution = 4
        
    def onEOL(self):
        pass
    
    def typewrite(self):
        if self.caret_pos <= len(self.line):
            self.text = self.line[0:self.caret_pos]
            self.caret_pos += 1
            
            Sound.play_modulated(self.sounds["keystroke"])
        
class Dialog(Typewriter):
    def __init__(self, own):
        Typewriter.__init__(self, own)
        self.fade = False
        self.init_time = bge.logic.getRealTime()
    
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
        
    def handle_fade(self):
        now = bge.logic.getRealTime() - self.init_time
        if self.fade <= now:
            self.color[3] -= .01
            if self.color[3] <= 0:
                self.endObject()
        
    def main(self):
        self.typewrite()
        self.align_to_camera()
        self.adjust_position()
        if self.fade is not False:
            self.handle_fade()
    
        
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
    
    
    