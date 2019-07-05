class PoliceNode:
    def __init__(self, policeId, fineAmt):
        self.policeId = policeId
        self.fineAmt=fineAmt
        self.left = None
        self.right = None


class PoliceTree:
    def init_root(self, policeId, fineAmt):
        self.rootNode = PoliceNode(policeId,fineAmt);