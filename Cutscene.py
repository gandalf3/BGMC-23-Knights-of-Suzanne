import bge
from Typewriter import Dialog

class CutsceneEvent():
    def __init__(self, time, func):
        self.time = time
        self.func = func
        self.finished = False
        
    def execute(self):
        self.func()

class Cutscene():
    def __init__(self):
        self.events = []
        self.started = False
        
    def register_event(self, time):
        def get_event(func):
            self.events.append(CutsceneEvent(time, func))
            return func
        return get_event
        
        
    def run(self):
        if not self.started:
            self.started = True
            self.t_zero = bge.logic.getRealTime()
            
        now = bge.logic.getRealTime() - self.t_zero
        
        for evt in self.events:
            if not evt.finished and evt.time <= now:
                evt.execute()
                evt.finished = True
        
    