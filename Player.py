import bge
from mathutils import Vector


class Player(bge.types.KX_GameObject):
    def __init__(self, own):
        self.player_control = False
        self.inertia = .1
        self.jump_force = 3
        self.speed = 1
        self.speedfac = .05
        self.direction = 1
        
    def move(self):
        if self.sensors["Left"].positive:
            self.speed = 1
            self.direction = -1
        if self.sensors["Right"].positive:
            self.speed = 1
            self.direction = 1
        if self.sensors["Jump"].positive and self.sensors["Collision"].positive:
            self.setLinearVelocity((0,0,self.jump_force))
        
        self.worldPosition.x += self.speed*self.direction*self.speedfac
        self.speed *= self.inertia
        
        if not self.children["PlayerVisual"].isPlayingAction():
            self.children["PlayerVisual"].playAction("PlayerWalkcycle", 1, 30, play_mode=bge.logic.KX_ACTION_MODE_LOOP, speed=2)
        if self.speed <= .01:
            self.children["PlayerVisual"].stopAction()
            

    def look(self):
        self.alignAxisToVect((0,0,1), 2, 1)
        self.alignAxisToVect((-self.direction,0,0), 1, .4)
            
    
    def main(self):
        self.move()
        self.look()
        
        
def run(cont):
    own = cont.owner
    
    if "player_init" not in own:
        own["player_init"] = True
        own = Player(own)
        
    own.main()