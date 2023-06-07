class Player:
    Game_Name= 'Lost in Life'
    
    Player_List = []
    
    def __init__(self, name, hp, attack, defense, abilities, companion):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.abilities = abilities
        self.companion = companion
        Player.Player_List.append(self)
        
    def PlayerInfo(self):
        print(f'Player Name : {self.name}\n hp: {self.hp}\n Attack : {self.attack}\n Defense : {self.defense}\n Abilities : {self.abilities}')
    
    def TakeDamage(self, dmg):
        self.hp = self.hp - (dmg - self.defense)
        print(f'Player {self.name} takes {dmg}! \n Current HP : {self.hp}')
        
    @classmethod
    def GetAllPlayers(cls):
        for player in cls.Player_List:
            print(player.name)

class Companion:
    
    def __init__(self, name, abilities, mana=100) -> None:
        self.name = name
        self.abilities = abilities
        self.mana = mana
        
    def PetAttack(self, target):
        self.mana -= 10
        print(f'{self.name} used {self.abilities[0]}, it cost 10 Mana.')
        target.hp = target.hp - (10 - target.defense)
        print(f'{self.name} Damaged {target.name} for {target.defense - 10}!')




Agumon = Companion('Agumon', ['Pepper Breath'])
Onyx = Companion('Onyx', ['Rock Smash'])

Agumon = Companion('Agumon', ['Pepper Breath'])
nudeMafia= Player('NudeMafia', 100, 10, 5, ['steal', 'dance', 'disappear'], Agumon)
coding= Player('Coding', 500, 90, 1000, ['debt', 'teach', 'hypnosis'], Onyx)


# nudeMafia.companion.PetAttack(coding)
# print(nudeMafia) #(output)<__main__.Player object at 0x000002334ACCE690>
# print(nudeMafia.name)#(output)NudeMafia

# nudeMafia.PlayerInfo()

# nudeMafia.TakeDamage(10)
# nudeMafia.TakeDamage(coding.attack)

# print(Player.Game_Name)
# nudeMafia.Game_Name = 'Lost in Life: After Air Force'
# print(nudeMafia.Game_Name)

Player.GetAllPlayers()


