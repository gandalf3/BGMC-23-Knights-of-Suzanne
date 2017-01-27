import bge
import random
import aud

def get_device():
    ctrl = bge.logic.getCurrentScene().objects["Control"]
    if "device" not in ctrl:
        ctrl["device"] = aud.device()
        ctrl["device"].distance_model = aud.AUD_DISTANCE_MODEL_LINEAR
    
    return ctrl["device"]

def play_modulated(factory):
        device = get_device()
        # Play the sound, using the sound_device and factory created earlier
        handle = device.play(factory)
        handle.relative = False
        handle.distance_maximum = 100
        handle.distance_reference = 2
        # Pick a random offset between -.3 and +.3 to be applied to the pitch later
        handle.pitch = random.randrange(90, 110)*.01
        
def update_handle(handle):
    # Tell aud handle the most recent location/orientation/velocity of this coin object
    self.sound_handle.location = self.worldPosition
    self.sound_handle.orientation = self.worldOrientation.to_quaternion()
    self.sound_handle.velocity = self.worldLinearVelocity
    
def update_device(device):
    # Tell aud device the most recent location/orientation/velocity of our listener object
    self.sound_device.listener_location = self.listener.worldPosition
    self.sound_device.listener_orientation = self.listener.worldOrientation.to_quaternion()
    self.sound_device.listener_velocity = self.listener.worldLinearVelocity
    
def load_factory(filename, buffer=False):
    f = aud.Factory.file(bge.logic.expandPath("//sounds/" + filename))
    
    if buffer:
        return aud.Factory.buffer(f)
    else:
        return f