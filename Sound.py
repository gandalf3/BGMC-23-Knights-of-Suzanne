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
        
def update_handle(handle, ob):
    # Tell aud handle the most recent location/orientation/velocity of object
    handle.location = ob.worldPosition
    handle.orientation = ob.worldOrientation.to_quaternion()
    handle.velocity = ob.getLinearVelocity()
    
def update_device(ob):
    device = get_device()
    # Tell aud device the most recent location/orientation/velocity of our listener object
    device.listener_location = ob.worldPosition
    device.listener_orientation = ob.worldOrientation.to_quaternion()
    device.listener_velocity = ob.getLinearVelocity()
    
def load_factory(filename, buffer=False):
    f = aud.Factory.file(bge.logic.expandPath("//sounds/" + filename))
    
    if buffer:
        return aud.Factory.buffer(f)
    else:
        return f
    
def play(factory):
    device = get_device()
    # Play the sound, using the sound_device and factory created earlier
    handle = device.play(factory)
    handle.relative = False
    return handle
    
def cont_play(cont):
    own = cont.owner
    if "handle" not in own:
        own["factory"] = load_factory(own["sound"]).loop(-1)
        own["handle"] = play(own["factory"])
        own["handle"].distance_maximum = own.get("maxdist", 100)
        own["handle"].distance_reference = own.get("refdist", 2)
    update_handle(own["handle"], own)
    