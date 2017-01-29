import bge
from Typewriter import Dialog

class CutsceneEvent():
    def __init__(self, time, func):
        self.time = time
        self.func = func
        self.finished = False
        self.pause = False
        
    def execute(self):
        self.func()

class Cutscene():
    def __init__(self):
        self.events = []
        self.started = False
        
    def register_event(self, time, pause=False):
        def get_event(func):
            evt = CutsceneEvent(time, func)
            if pause:
                evt.pause = True
            self.events.append(evt)
            return func
        return get_event
        
        
    def run(self):
        if not self.started:
            self.started = True
            self.now = 0
            self.paused = False
            self.pause_after = None
            
        if self.paused:
            if bge.logic.mouse.events[bge.events.LEFTMOUSE]:
                self.paused = False
        else:
            self.now += 1
            #print(self.now/60)
            for id, evt in enumerate(self.events):
                
                #fast forward
                if not evt.finished:
                    evt.execute()
                    evt.finished = True
                
                if not evt.finished and evt.time <= self.now/60:

                    if self.pause_after is None or id == self.pause_after:
                        print("evt", id, "at", self.now/60)
                        evt.execute()
                        evt.finished = True
                    else:
                        self.paused = True
                        self.pause_after = None
                    
                    if evt.pause:
                        self.pause_after = id
            
    