import bge
import Sound
import Particles
import utils
from mathutils import Vector
import random

class Enemy(bge.types.KX_GameObject):
    
    sounds = {\
        "boil": Sound.load_factory("boiling.wav").loop(-1),
        "whistle": Sound.load_factory("steamwhistle.wav")
        }
    
    def __init__(self, own):
        self.health = 1
        self.cooldown_length = 4*60
        self.cooldown = self.cooldown_length
        self.attacking = False
        self.attack_timer = 0
        self.tic = 0
        self.boil_sound = Sound.play(self.sounds["boil"])
        self.boil_sound.volume = 0.3
        self.whistle = None
        self.tic = random.randint(0, 3*60)
        
        
    def behavior(self):
        if self.sensors["Near"].positive:
            self.attack()
        
    def release_steam(self):
        if not self.attacking:
            Particles.spawn_particle("steam", self.children["particle_reference"])
    
    def attack(self):
        if not self.attacking and self.cooldown <= 0:
            self.attacking = True
            self.attack_begin = bge.logic.getRealTime()
        
    def handle_attack(self):
        scn = bge.logic.getCurrentScene()
        
        self.attack_timer += 1
        stage_1 = 2*60
        vect_to = scn.objects["Player"].worldPosition.copy() - self.worldPosition.copy()
        if vect_to.length >= 2:
            vect_to = (scn.objects["Player"].worldPosition.copy() - self.worldPosition.copy())  - Vector((0,0,1))
        
        if self.attack_timer < stage_1:
            self.boil_sound.volume = utils.clamp(self.attack_timer/(stage_1))
            self.alignAxisToVect(vect_to, 2, .1)
        if self.attack_timer == stage_1:
            self.whistle = Sound.play_modulated(self.sounds["whistle"], 1, 1.05)
        if self.attack_timer >= stage_1:
            if self.attack_timer%3 == 0:
                p = Particles.spawn_particle("steam", self.children["particle_reference"])
                p.emit_direction = vect_to.normalized()
                p.emit_speed = 5
                p.focus = .2
                p.lifetime = 1*60
                p.scale = 5
            self.boil_sound.volume = utils.clamp(self.attack_timer/(stage_1))

            if not self.whistle.status:
                self.attacking = False
                self.attack_timer = 0
                self.cooldown = self.cooldown_length
            
    def die(self):
        if self.whistle:
            self.whistle.stop()
        if self.boil_sound:
            self.boil_sound.stop()
        self.endObject()
        
    
    def main(self):
        self.behavior()
        if self.attacking == True:
            self.handle_attack()
        else:
            self.alignAxisToVect((0,0,1), 2, .1)
        if self.tic%(3*60) >= (2.7*60):
            self.release_steam()
            
        Sound.update_handle(self.boil_sound, self)
        if self.whistle and self.whistle.status:
            Sound.update_handle(self.whistle, self)
        self.tic += 1
        self.cooldown -= 1
        
        if self.sensors["damage"].status == bge.logic.KX_SENSOR_ACTIVE:
            self.die()
                
        
            
        
        
        
class Teapot(Enemy):
    def __init__(self, own):
        Enemy.__init__(self, own)



def teapot(cont):
    own = cont.owner
    
    if "teapot_init" not in own:
        own = Teapot(own)
        own["teapot_init"] = True
    
    own.main()
