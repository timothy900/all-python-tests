# BROKEN
# 12/30/19
# testing with classes


class Robot:

    const = 2

    def __init__(self, name, health, atk, defn, spd):
        self.name = name
        self.health = health
        self.atk = atk
        self.defn = defn
        self.spd = spd


    def slash(self, reciever):
        slash_pwr = 10
    
        dmg = self.atk * slash_pwr
        dmg -= reciever.defn * Robot.const
        
        reciever.health += dmg
        print("{} hit {} for {} damage".format(self.name, reciever.name, dmg*-1))
        reciever.health = round(reciever.health, 1)



bebot = Robot("bebot" , 20, 3, 5, 1)
robort = Robot("robort", 30, 2, 1, 3)


def fight(one, two):
    print(two.health)
    Robot.slash(one, two)
    print(two.health)

fight(bebot, robort)





