import bge
from mathutils import Vector, noise
import random

steam_particles = ['Particle.001', 'Particle']
dust_particles = ['Particle.002', 'Particle.003']
prim_particles = ['Sphere', 'Cube.005', 'Cylinder.004', 'Cone']
#grass_particles

class Particle(bge.types.KX_GameObject):
    def __init__(self, own):
        self.init_time = bge.logic.getRealTime()
        self.lifetime = .7*60
        self.elapsed_tics = 0
        
    def control_size(self):
        s = (self.elapsed_tics/self.lifetime)
        self.localScale.xyz = -(((s-.5)*2)**2)+1
        
    def main(self):
        self.elapsed_tics += 1
        if self.elapsed_tics >= self.lifetime:
            self.endObject()
        
class SteamParticle(Particle):
    def __init__(self, own):
        Particle.__init__(self, own)
        self.emit_direction = Vector((0,0,1))
        self.emit_speed = 1
    #    print()
        self.setLinearVelocity(self.emit_direction.lerp(noise.random_unit_vector(), .3))
        
    def main(self):
        Particle.main(self)
        self.control_size()
        scn = bge.logic.getCurrentScene()
        #counter gravity and float a bit
        self.applyForce(-scn.gravity*1.1)
            
            
class PrimParticle(Particle):
    def __init__(self, own):
        Particle.__init__(self, own)
        self["prim_init"] = True
        self.emit_direction = Vector((0,0,1))
        self.lifetime = 3*60
        self.emit_speed = 0
        self.first_tic = False

        
    def main(self):
        Particle.main(self)
        scn = bge.logic.getCurrentScene()
        if not self.first_tic:
            self.first_tic = True
            self.setLinearVelocity(self.emit_direction*self.emit_speed)
            self.setAngularVelocity(noise.random_unit_vector()*5)
        
        self.applyForce(-scn.gravity*.4)
        
        
def steam(cont):
    own = cont.owner
    
    if "steam_init" not in own:
        own = SteamParticle(own)
        own["steam_init"] = True
    
    own.main()

def prim(cont):
    own = cont.owner
    
    if "prim_init" not in own:
        own = PrimParticle(own)
        own["prim_init"] = True
    
    own.main()

        
def spawn_particle(type, reference):
    scn = bge.logic.getCurrentScene()
    if type == "steam":
        ob = random.choice(steam_particles)
        scn.addObject(ob, reference)
    elif type == "prim":
        ob = random.choice(prim_particles)
        particle = PrimParticle(scn.addObject(ob, reference))
    
        return particle
        