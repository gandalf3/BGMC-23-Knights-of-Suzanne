import bge
from mathutils import Vector
import Sound
from utils import lerp, Plane, get_mouse_on_plane, clamp
from math import copysign
import Particles

class Player(bge.types.KX_GameObject):
    def __init__(self, own):
        self.player_control = True
        self.inertia = .1
        self.jump_force = 5
        self.jump_n = 0
        self.jump_cooldown = .4*60
        self.jump_coolness = self.jump_cooldown
        self.speed = 1
        self.speedfac = .05
        self.direction = 1
        self.tic = 0
        self.target_pos = None
        self.look_direction = None
        self.look_target = None
        self.action_stop = False
        
        self.abilities = ['attack']
        self.attack1_cooldown = .2*60
        self.attack1_coolness = self.attack1_cooldown
        self.attack2_chargetime = 60
        self.attack2_charge = 0
        
        self.to_mouse = None
        
        bge.render.showMouse(True)
        self.xlock = False
        
        if not bge.logic.globalDict["accomplishments"]["sword"]:
            self.children["PlayerVisual"].children["Sword"].visible = False
        
    def move(self):
        model = self.children["PlayerVisual"]
        
        if self.player_control:
            if self.sensors["Left"].positive:
                self.speed = 1
                self.direction = -1
            if self.sensors["Right"].positive:
                self.speed = 1
                self.direction = 1
            if self.sensors["Jump"].positive:
                self.jump()
            if self.sensors["Collision"].positive:
                if self.jump_coolness <= 0:
                    self.jump_n = 0
                hit_o = self.sensors["Collision"].hitObject
                if hit_o:
                    obj, point, normal = self.rayCast(hit_o, None, 1, "jumpable")
                    if obj and obj == hit_o:
                        # is jump surface vertical?
                        if abs(normal.dot((0,0,1))) < .1:
                            self.xlock = self.worldPosition.x
                            self.xlock_normal = normal
                
            self.worldLinearVelocity.x = clamp(self.worldLinearVelocity.x + self.speed*self.direction*.5, -3, 3)
            self.look(Vector((self.direction, 0, 0)))
            self.speed *= self.inertia
            #self.worldLinearVelocity.x *= .002
            
#            if self.xlock:
#                self.worldPosition.x = self.xlock
#                self.worldLinearVelocity.z *= .9
        
            
        
            if self.speed > .01:
                self.action_stop = False
                if not model.isPlayingAction(0) and not model.isPlayingAction(1):
                    model.playAction("PlayerWalkcycle", 1, 30)
                model.setActionFrame(self.tic%30)
                
            else:
                self.lerp_action_to(7)
            
        else:
            if self.target_pos is not None:
                self.direction = (self.target_pos - self.worldPosition.copy()).x
                self.worldPosition.x += (copysign(min(self.speed*self.speedfac*7, abs(self.direction)), self.direction))
            self.lerp_action_to(7)
            
            
            
    def jump(self):
        model = self.children["PlayerVisual"]
        #print(self.jump_n, self.jump_coolness)
        
        if self.jump_coolness <= 0:
            if self.sensors["Collision"].positive:
                jump_vector = Vector((0,0,self.jump_force))
                self.jump_coolness = self.jump_cooldown
#        if self.jump_n < 2 and self.jump_coolness <= self.jump_cooldown*.3:
#            if self.sensors["Collision"].positive:
#                self.jump_n += 1
#            else:
#                self.jump_n += 2
#                
#            jump_vector = Vector((0,0,self.jump_force*(1 if self.jump_n <= 1 else 1.5)))
#        
#            # walljump
#            if self.xlock:
#                self.xlock = False
#                jump_vector += self.xlock_normal*4
#                self.jump_n += 2

#            print(jump_vector)
                self.worldLinearVelocity += jump_vector
                
        
                model.stopAction(0)
                model.stopAction(1)
                model.playAction("PlayerJump", 1, 30, layer=1, speed=2)
        
            
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
#        if self.look_target is not None:
#            print("targeting")
#            vect = self.worldPosition.copy() - self.look_target
#            self.alignAxisToVect(vect, 1, .4)
        if self.look_direction is not None:
            self.alignAxisToVect(-self.look_direction, 1, 1)
        else:
            self.alignAxisToVect((0,-1,0), 1, .4)
    
    def look(self, direction):
        d = Vector(direction)
        self.direction = copysign(1, d.x)
        self.look_direction = d.copy()
        
    def lookat(self, ob):
        print("looking")
        self.look(ob.worldPosition.copy())
    
    def goto(self, spot):
        self.look_target = spot.copy()
        if spot.x - self.worldPosition.x < 0:
            spot.x += .5
        else:
            spot.x -= .5
            
        self.target_pos = spot
        print(self.name, "going to", self.target_pos)
        
            
    
    def attack1(self):
        model = self.children["PlayerVisual"]
        sword = model.children["Sword"]
        
        if self.sensors["Mouse1"].positive:
            pass
        
    def attack2(self):
        model = self.children["PlayerVisual"]
        sword = model.children["Sword"]
        
        if self.sensors["Mouse2"].positive:
            if self.attack2_charge < self.attack2_chargetime:
                self.attack2_charge += 1
        else:
            if self.attack2_charge > self.attack2_chargetime/25:
                prim = Particles.spawn_particle("prim", sword)
                if self.to_mouse:
                    prim.emit_direction = self.to_mouse
                power = ((self.attack2_charge/self.attack2_chargetime)**(1/3))
                prim.emit_speed = power*3
                prim.localScale.xyz = power*.5
                self.attack2_charge = 0
            #prim.emit_direction =
            
            
    def handle_sword(self):
        model = self.children["PlayerVisual"]
        sword = model.children["Sword"]
        
        if self.to_mouse:
            sword.alignAxisToVect(-self.to_mouse, 1, .2)
            sword.alignAxisToVect(model.worldOrientation[0], 2, 1)
            
            
    def die(self):
        self.worldPosition = (0,0,0)
    
    def main(self):
        self.move()
        self.handle_look()
        self.handle_lerp_action_to()
        self.handle_sword()
        if "attack" in self.abilities:
            self.attack1()
            self.attack2()
            
        xz = Plane(Vector((0, 0, 0)), Vector((0, -1, 0)))
        mouse = get_mouse_on_plane(xz, self.sensors["Mouse"])
        if mouse:
            self.to_mouse = mouse - self.worldPosition
            
        if self.jump_coolness >= 0:
            self.jump_coolness -= 1
            
        if self.sensors["Steam"].status == bge.logic.KX_SENSOR_ACTIVE:
            self.damage_tic += 1
            if self.damage_tic >= 1*60:
                self.die()
        else:
            self.damage_tic = 0
        
        self.tic += 1
        
        
def run(cont):
    own = cont.owner
    
    if "player_init" not in own:
        own["player_init"] = True
        own = Player(own)
        
    own.main()
