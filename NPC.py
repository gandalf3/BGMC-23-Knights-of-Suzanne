import bge
from Typewriter import Dialog
from mathutils import Vector
from SceneManage import getScene

class NPC(bge.types.KX_GameObject):
    def __init__(self, own):
        self.inertia = .1
        self.speed = 1
        self.speedfac = .05
        self.direction = 1
        self.textbox = None
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

    def look(self, direction):
        self.look_direction = direction
    
    def handle_look(self):
        self.alignAxisToVect((0,0,1), 2, 1)
        self.alignAxisToVect(self.look_direction, 1, .2)
        
    def say(self, words, emphasis=False):
        print(self.name, "says")
        if self.textbox is None or self.textbox.invalid:
            tscn = getScene("TextOverlay")
            self.textbox = Dialog(tscn.addObject("GenericDialog", self))
            print("added new textbox")
        self.textbox.target_pos = self.worldPosition
        if emphasis:
            self.textbox.localScale *= 2
        self.textbox.write(words)
        self.textbox.fade = 2
    
    def talk(self):
        if self.sensors["PlayerProximity"].status == bge.logic.KX_SENSOR_JUST_ACTIVATED:
            self.say(self.dialog)
        if self.sensors["PlayerProximity"].status == bge.logic.KX_SENSOR_JUST_DEACTIVATED:
            if not self.textbox.invalid:
                self.textbox.fade = 0
            self.textbox = None
    
    def draw_attention(self):
        self.playAction("DrawAttention", 1, 17)
            
    
    def main(self):
        if not bge.logic.getCurrentScene().objects["Control"].get("running_cutscene", 0):
            self.talk()
            #self.move()
            #self.look()
        
        
def run(cont):
    own = cont.owner
    
    if "NPC_init" not in own:
        own["NPC_init"] = True
        own = NPC(own)
        
    own.main()