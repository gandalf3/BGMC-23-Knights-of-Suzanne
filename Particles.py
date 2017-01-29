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
        self["particle_init"] = True
        self.lifetime = .7*60
        self.elapsed_tics = 0
        self.first_tic = True
        
    def control_size(self):
        s = (self.elapsed_tics/self.lifetime)
        self.localScale.xyz = -(((s-.5)*2)**2)+1
        
    def main(self):
        if self.elapsed_tics >= 2:
            self.first_tic = False
        self.elapsed_tics += 1
        if self.elapsed_tics >= self.lifetime:
            self.endObject()
        
class SteamParticle(Particle):
    def __init__(self, own):
        Particle.__init__(self, own)
        self.emit_direction = Vector((0,0,1))
        self.emit_speed = 1
        self.focus = .3
    #    print()
        
    def main(self):
        Particle.main(self)
        if self.first_tic:
            print(self.emit_direction, self.emit_speed)
            self.setLinearVelocity(self.emit_direction.lerp(noise.random_unit_vector(), self.focus)*self.emit_speed)
            
        self.control_size()
        scn = bge.logic.getCurrentScene()
        #counter gravity and float a bit
        self.applyForce(-scn.gravity*1.1)
            
            
class PrimParticle(Particle):
    def __init__(self, own):
        Particle.__init__(self, own)
        self.emit_direction = Vector((0,0,1))
        self.lifetime = 3*60
        self.emit_speed = 0

        
    def main(self):
        Particle.main(self)
        scn = bge.logic.getCurrentScene()
        if self.first_tic:
            self.setLinearVelocity(self.emit_direction*self.emit_speed)
            self.setAngularVelocity(noise.random_unit_vector()*5)
        
        self.applyForce(-scn.gravity*.4)
        
        
def steam(cont):
    own = cont.owner
    
    if "particle_init" not in own:
        own = SteamParticle(own)
        own["particle_init"] = True
    
    own.main()

def prim(cont):
    own = cont.owner
    
    if "particle_init" not in own:
        own = PrimParticle(own)
        own["particle_init"] = True
    
    own.main()

        
def spawn_particle(type, reference):
    scn = bge.logic.getCurrentScene()
    if type == "steam":
        ob = random.choice(steam_particles)
        particle = SteamParticle(scn.addObject(ob, reference))
    elif type == "prim":
        ob = random.choice(prim_particles)
        particle = PrimParticle(scn.addObject(ob, reference))
    
    return particle
        