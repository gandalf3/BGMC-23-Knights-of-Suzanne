from NPC import NPC
import DialogText

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
        
def run(cont):
    own = cont.owner
    
    if "NPC_init" not in own:
        own["NPC_init"] = True
        if own.name == "Anne":
            own = Anne(own)
        elif own.name == "Sir_Sergey":
            own = Sir_Sergey(own)
        
    own.main()