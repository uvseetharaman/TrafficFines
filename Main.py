from PoliceFines import PoliceFines
from ds.PoliceTree import PoliceTree


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
    hashTable = pf.initializeHash()
    # 2) Create binary tree
    binaryTree = PoliceTree()
    binaryTree.init_root(policeId=0, fineAmt=0)

    f = open('inputPS3.txt', 'r')
    for line in f:
        # print(line, end='')
        splits = line.split('/')
        if len(splits) != 3:
            raise Exception("expecting police id, license number and fine amount in each row")
        policeId = splits[0].strip()
        licenseNumber = splits[1].strip()
        fineAmount =int(splits[2].strip())

        pf.insertHash(hashTable, licenseNumber)
    f.close()
    pf.printViolators(hashTable);




