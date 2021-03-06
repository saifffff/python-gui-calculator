class Player:
    game = "football"
    leauge = "UEFA Champions leauge"

    def __init__(self,pname,pteam,pcountry,pjersey):
        self.name = pname
        self.team = pteam
        self.country = pcountry
        self.jersey = pjersey
    
    def printDetails(self):
        return f"Name : {self.name}\nTeam : {self.team}\nCountry : {self.country}\nJersey No : {self.jersey}"
    
    @classmethod
    def changeLeauge(cls,cleauge):
        cls.leauge=cleauge
    # class method as an alt constructor
    @classmethod
    def createInstance(cls,string):
        details = string.split("-")
        # return cls(details[0],details[1],details[2],details[3])
        return cls(*string.split("-"))
    # static methods are used when we do not need class or even self(objects) in the processing
    @staticmethod
    def useless(string):
        return string

ronaldo = Player("Cristiano","Manchester United","Portugal",7)
messi = Player.createInstance("Lionel-PSG-Argentina-10")

# print(messi.printDetails())
# print(messi.useless("hi i am useless"))

class Sportsman(Player):
    pass

kaka = Sportsman.createInstance("Kaka-Barca-Brasil-10")

print(kaka.printDetails())