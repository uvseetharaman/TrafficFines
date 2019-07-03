from PoliceFines import PoliceFines


class PoliceNode:
    def __init__(self, policeId, fineAmt):
        self.policeId = policeId
        self.fineAmt=fineAmt
        self.left = None
        self.right = None


if __name__ == '__main__':
    print("start")
    pf = PoliceFines()
    # 1) Create hash table with the given hash function and call related functions
    pf.initializeHash()
    # 2) Create binary tree
    root = PoliceNode()



