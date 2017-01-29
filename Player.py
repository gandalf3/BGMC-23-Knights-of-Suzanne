import bge
from mathutils import Vector
import Sound
from utils import lerp
from math import copysign

class Player(bge.types.KX_GameObject):
    def __init__(self, own):
        self.player_control = True
        self.inertia = .1
        self.jump_force = 3
        self.speed = 1
        self.speedfac = .05
        self.direction = 1
        self.tic = 0
        self.target_pos = None
        self.look_direction = None
        self.action_stop = False
        
    def move(self):
        model = self.children["PlayerVisual"]
        
        if self.player_control:
            if self.sensors["Left"].positive:
                self.speed = 1
                self.direction = -1
            if self.sensors["Right"].positive:
                self.speed = 1
                self.direction = 1
            if self.sensors["Jump"].positive and self.sensors["Collision"].positive:
                self.setLinearVelocity((0,0,self.jump_force))
                
                model.stopAction(0)
                model.stopAction(1)
                model.playAction("PlayerJump", 1, 30, layer=1, speed=2)
                
            self.worldPosition.x += self.speed*self.direction*self.speedfac
            self.look(Vector((self.direction, 0, 0)))
            self.speed *= self.inertia
        
            
        
            if self.speed > .01:
                self.action_stop = False
                if not model.isPlayingAction(0) and not model.isPlayingAction(1):
                    model.playAction("PlayerWalkcycle", 1, 30)
                model.setActionFrame(self.tic%30)
                
            else:
                self.lerp_action_to(7)
            
        else:
            if self.target_pos is not None:
                self.direction = self.target_pos - self.worldPosition.copy()
                self.worldPosition.x += (copysign(min(self.speed*self.speedfac*5, abs(self.direction.x)), self.direction.x))
            self.lerp_action_to(7)
            
            
            
    def lerp_action_to(self, frame):
        if self.action_stop is False:
            self.action_started_to_stop = bge.logic.getRealTime()
            self.action_stop = frame
        
    def handle_lerp_action_to(self):
        model = self.children["PlayerVisual"]
        if self.action_stop is not False:
            new_frame = lerp(model.getActionFrame(), self.action_stop, min((bge.logic.getRealTime() - self.action_started_to_stop), 1))
            model.setActionFrame(new_frame)
            
    
    def handle_look(self):
        self.alignAxisToVect((0,0,1), 2, 1)
        if self.look_direction is not None:
            self.alignAxisToVect((-self.look_direction.x,0,0), 1, .4)
        else:
            self.alignAxisToVect((0,-1,0), 1, .4)
    
    def look(self, direction):
        self.direction = copysign(1, direction.x)
        self.look_direction = direction
        
    def lookat(self, ob):
        self.look(ob.worldPosition.copy())
    
    def goto(self, spot):
        self.look_target = spot.copy()
        if spot.x - self.worldPosition.x < 0:
            spot.x += .5
        else:
            spot.x -= .5
            
        self.target_pos = spot
        print(self.name, "going to", self.target_pos)
        
            
    
    def main(self):
        self.move()
        self.handle_look()
        self.handle_lerp_action_to()
        self.tic += 1
        
        
def run(cont):
    own = cont.owner
    
    if "player_init" not in own:
        own["player_init"] = True
        own = Player(own)
        
    own.main()