import bge
from Typewriter import Dialog
from mathutils import Vector
from math import copysign
from SceneManage import getScene

class NPC(bge.types.KX_GameObject):
    def __init__(self, own):
        self.inertia = .1
        self.speed = 1
        self.speedfac = .05
        self.direction = 1
        self.textbox = None
        self.dialog = ""
        self.target_pos = None
        self.look_target = None
        self.look_direction = None
        
    def goto(self, spot):
        self.look_target = spot.copy()
        if spot.x - self.worldPosition.x < 0:
            spot.x += .5
        else:
            spot.x -= .5
            
        self.target_pos = spot
        print(self.name, "going to", self.target_pos)
    
    def move(self):
        if self.target_pos is not None:
            self.direction = self.target_pos - self.worldPosition.copy()
            #self.worldPosition.x += copysign(min(self.speed*self.speedfac, abs(self.direction.x)), self.direction.x)
            self.setLinearVelocity((copysign(min(self.speed*self.speedfac, abs(self.direction.x)), self.direction.x)*70, 0, 0))
        
#        if not self.isPlayingAction():
#            self.playAction("PlayerWalkcycle", 1, 30, play_mode=bge.logic.KX_ACTION_MODE_LOOP, speed=2)
#        if self.speed <= .01:
#            self.stopAction()

    def look(self, direction):
        self.look_direction = direction
    
    def handle_look(self):
        if self.look_direction is not None:
            self.alignAxisToVect((0,0,1), 2, 1)
            self.alignAxisToVect(self.look_direction, 1, .2)
        elif self.look_target is not None:
            self.alignAxisToVect((0,0,1), 2, 1)
            self.alignAxisToVect(self.worldPosition - self.look_target, 1, .2)
        
    def say(self, words, emphasis=False):
        if self.textbox is not None:
            try:
                self.textbox.worldPosition
            except SystemError:
                tscn = getScene("TextOverlay")
                self.textbox = Dialog(tscn.addObject("GenericDialog", self))
                print("added new textbox")
        else:
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
        self.children[0].playAction("DrawAttention", 1, 17)
            
    
    def main(self):
        if not bge.logic.getCurrentScene().objects["Control"].get("running_cutscene", 0):
            self.talk()
            #self.look()
        self.move()
        self.handle_look()
        
        
def run(cont):
    own = cont.owner
    
    if "NPC_init" not in own:
        own["NPC_init"] = True
        own = NPC(own)
        
    own.main()