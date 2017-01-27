import bge
from Typewriter import Dialog, Typewriter
from mathutils import Vector
from SceneManage import getScene

class NPC(bge.types.KX_GameObject):
    def __init__(self, own):
        self.inertia = .1
        self.speed = 1
        self.speedfac = .05
        self.direction = 1
        self.textbox = False
        self.dialog = ""
        
    def move(self):
        if self.sensors["Left"].positive:
            self.speed = 1
            self.direction = -1
        if self.sensors["Right"].positive:
            self.speed = 1
            self.direction = 1
        
        self.worldPosition.x += self.speed*self.direction*self.speedfac
        self.speed *= self.inertia
        
        if not self.children["PlayerVisual"].isPlayingAction():
            self.children["PlayerVisual"].playAction("PlayerWalkcycle", 1, 30, play_mode=bge.logic.KX_ACTION_MODE_LOOP, speed=2)
        if self.speed <= .01:
            self.children["PlayerVisual"].stopAction()

    def look(self):
        self.alignAxisToVect((0,0,1), 2, 1)
        self.alignAxisToVect((-self.direction,0,0), 1, .2)
    
    def talk(self):
        if self.sensors["PlayerProximity"].status == bge.logic.KX_SENSOR_JUST_ACTIVATED:
            print("PREPARE TO TALK")
            if not self.textbox:
                tscn = getScene("TextOverlay")
                print(tscn)
                if tscn:
                    self.textbox = Dialog(tscn.addObject("GenericDialog"))
            self.textbox.write(self.dialog)
            self.textbox.target_pos = self.worldPosition
            
        if self.sensors["PlayerProximity"].status == bge.logic.KX_SENSOR_JUST_DEACTIVATED:
            if not self.textbox.invalid:
                self.textbox.endObject()
            self.textbox = False
            print("GET TALKED")
            
    
    def main(self):
        self.talk()
        #self.move()
        #self.look()
        
        
def run(cont):
    own = cont.owner
    
    if "NPC_init" not in own:
        own["NPC_init"] = True
        own = NPC(own)
        
    own.main()