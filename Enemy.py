import bge
import Particles
#import

class Enemy(bge.types.KX_GameObject):
    def __init__(self, own):
        self.health = 1
        self.cooldown_length = 60*2
        self.attacking = False
        self.cooldown = self.cooldown_length
        
        
    def behavior(self):
        if self.sensors["Near"].positive:
            self.attack()
        
    
    def attack(self):
        if not self.attacking:
            self.attacking = True
            self.attack_begin = bge.logic.getRealTime()
        
    def handle_attack(self):
        attack_duration = bge.logic.getRealTime() - self.attack_begin
        if attack_duration < .3:
            Particles.spawn_particle("steam", self.children["particle_reference"])
        else:
            self.cooldown -= 1
            if self.cooldown <= 0:
                self.attacking = False
                self.cooldown = self.cooldown_length
            
        
        
    
    def main(self):
        self.behavior()
        if self.attacking == True:
            self.handle_attack()
        
        
        
class Teapot(Enemy):
    def __init__(self, own):
        Enemy.__init__(self, own)



def teapot(cont):
    own = cont.owner
    
    if "teapot_init" not in own:
        own = Teapot(own)
        own["teapot_init"] = True
    
    own.main()
