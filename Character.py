from NPC import NPC
import DialogText

class Frank(NPC):
    def __init__(self, own):
        NPC.__init__(self, own)
        self.full_name = "Frank"
        self.dialoglist = DialogText.Frank
        self.dialog = self.dialoglist["first_meeting"]

class Anne(NPC):
    def __init__(self, own):
        NPC.__init__(self, own)
        self.full_name = "Anne"
        self.dialoglist = DialogText.Anne
        self.dialog = self.dialoglist["first_meeting"]
        
class Sir_Sergey(NPC):
    def __init__(self, own):
        NPC.__init__(self, own)
        self.full_name = "Sir Sergey"
        
    def main(self):
        NPC.talk
        
def run(cont):
    own = cont.owner
    
    if "NPC_init" not in own:
        own["NPC_init"] = True
        if own.name == "Anne":
            own = Anne(own)
        elif own.name == "Sir_Sergey":
            own = Sir_Sergey(own)
        elif own.name == "Frank":
            own = Frank(own)
    
    own.main()