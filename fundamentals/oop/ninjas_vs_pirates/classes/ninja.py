
class Ninja:

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
        self.shurikens = 5
        self.slice = 5
    
    def show_stats(self):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , pirate):
        pirate.health -= self.strength
        print(f"{self.name} attacked {pirate.name} for {self.strength} damage!")
        return self
    
    def shuriken(self, pirate):
        if self.shurikens == 0:
            print("No shurikens left")
            return False
        else:
            shuriken_damage = self.strength*1.5
            pirate.health -= shuriken_damage
            self.shurikens -= 1
            print(f"\n{self.name} threw a shuriken at {pirate.name} for {int(shuriken_damage)} and has {self.shurikens} left")
            return self
        
    def pizza(self):
        if self.slice == 0:
            print("I need more pizza!")
        else:
            self.health += 10
            self.slice -= 1
            print(f"\n{self.name} ate a slice of pizza and health is {self.health}")
            return self
