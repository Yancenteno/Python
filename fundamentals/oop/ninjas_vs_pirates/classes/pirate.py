
class Pirate:

    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100
        self.bullets = 3
        self.bottles = 4

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack ( self , ninja ):
        ninja.health -= self.strength
        print(f"{self.name} attacked {ninja.name} for {self.strength} damage!\n")
        return self
    
    def pistol(self, ninja):
        if self.bullets == 0:
            print("Out of ammo!")
            return False
        else:
            pistol_damage = self.strength*2
            ninja.health -= (self.strength*2)
            self.bullets -= 1
            print(f'\n{self.name} shot at {ninja.name} for {int(pistol_damage)}')
            return self
    
    def rum(self):
        if self.bottles == 0:
            print("Out of booze!")
        else:
            self.health += 15
            self.bottles -= 1
            return self