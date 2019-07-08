class PoliceFines:

    def initializeHash(self):
        print("initializeHash")
        self.hashTable = {}
        return {}

    def insertHash(self, driverhash : dict, lic):
        print("insertHash")
        if lic in driverhash:
            driverhash[lic] = driverhash[lic] + 1
        else:
            driverhash[lic] = 1

    def printViolators(self, driverhash):
        print("printViolators")
        f = open("violators.txt","w")
        for i in driverhash:
            if driverhash[i]>=3:
                f.write(i + ", " + str(driverhash[i]))
        f.close()

    def destroyHash(driverhash):
        print("destroyHash")

    def insertByPoliceId(policeRoot, policeId, amount):
        print("insertByPoliceId")

    def reorderByFineAmount(policeRoot):
        print("reorderByFineAmount")

    def printBonusPolicemen(policeRoot):
        print("printBonusPolicement")

    def destroyPoliceTree(policeRoot):
        print("destroyPoliceTree")

    def printPoliceTree(policeRoot):
        print("printPoliceTree")
