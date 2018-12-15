class Member:
    def __init__(self, ins_type, player_name):
        self.ins = ins_type
        self.pl = player_name

    def getInstrument(self):
        return self.ins

    def getPlayer(self):
        return self.pl

    def setInstrument(self, instrument):
        self.nins = instrument

    def setPlayer(self, player):
        self.npl = player

    def __str__(self):
        return str(self.pl) + " plays " + str(self.ins)

    def __eq__(self,rhand):
        if self.ins.lower() == rhand.ins.lower() and self.pl.lower() == rhand.pl.lower():
            return True
        else:
            return False

class Band:
    def __init__(self, band_name, member_list):
        self.name = band_name
        self.ml = member_list

    def getBandName(self):
        return self.name

    def getPlayers(self):
        player_list = []
        for i in self.ml:
            player_list.append(i.getPlayer().lower())
        print(player_list)

    def getInstruments(self):
        dic = {}
        for j in self.ml:
            idx = j.getInstrument().lower()
            if idx in dic:
                dic[idx] += 1
            else:
                dic[idx] = 1
        print(dic)

    def addMember(self, member):
        self.ml.append(member)

    def removeMember(self,member):
        nlst = []
        for i in range(0,len(self.ml)):
            if self.ml[i] != member:
                nlst.append(self.ml[i])
        self.ml = nlst

    def __str__(self):
        astr = self.name +":\n"
        for i in range(0,len(self.ml)):
            astr = astr + str(self.ml[i]) + "\n"
        return str(astr)

    def findPlayer(self,player):
        for k in range(0,len(self.ml)):
            if player in str(self.ml[k]):
                a = True
            else:
                a = False
        if a == True:
            print(self.ml[k])
        else:
            print(self.name, "does not have any players named", player)

    def findInstrument(self,instrument):
        for h in range(0,len(self.ml)):
            if instrument in str(self.ml[h]):
                b = True
            else:
                b = False
        if b == True:
            print(self.ml[h])
        else:
          print(self.name, "does not have any", instrument, "players")
