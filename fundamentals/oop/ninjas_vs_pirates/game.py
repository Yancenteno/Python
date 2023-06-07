from classes.ninja import Ninja
from classes.pirate import Pirate

michelangelo = Ninja("Michelanglo")

jack_sparrow = Pirate("Jack Sparrow")


while michelangelo.health > 0 and jack_sparrow.health > 0:
    player_input = ""
    choice_input = ""
    while not choice_input =="Pirate" and not choice_input == "Ninja":
        choice_input = input("Choose a character class:\nPirate\nNinja\n")
        if choice_input == "Ninja":
            print("\nYou picked Michelangelo\n")
            while not player_input == "1" and not player_input == "2":
                player_input = input("Choose an action:\n1)Attack\n2)Shuriken Attack\n3)Pizza\n")
                if player_input == "1":
                    michelangelo.attack(jack_sparrow).show_stats()
                    jack_sparrow.attack(michelangelo).show_stats()
                    player_input= ""
                elif player_input == "2":
                    michelangelo.shuriken(jack_sparrow).show_stats()
                    jack_sparrow.pistol(michelangelo).show_stats()
                    player_input= ""
                elif player_input == "3":
                    michelangelo.pizza().show_stats()
                    jack_sparrow.rum().show_stats()
                    player_input= ""
                else:
                    print("\nChoose a valid action\n")
                if michelangelo.health <= 0:
                    print("Jack Sparrow won!")
                    break
                elif jack_sparrow.health <= 0:
                    print("Michelangelo won!")
                    break
                else:
                    print("Match Continues")
        elif choice_input == "Pirate":
            print("You picked Jack Sparrow")
            while not player_input == "1" and not player_input == "2":
                player_input = input("Choose an action:\n1)Attack\n2)Pistol\n3)Rum\n")
                if player_input == "1":
                    jack_sparrow.attack(michelangelo).show_stats()
                    michelangelo.attack(jack_sparrow).show_stats()
                    player_input= ""
                elif player_input == "2":
                    jack_sparrow.pistol(michelangelo).show_stats()
                    michelangelo.shuriken(jack_sparrow).show_stats()
                    player_input= ""
                elif player_input == "3":
                    jack_sparrow.rum().show_stats()
                    michelangelo.pizza().show_stats()
                    player_input= ""
                else:
                    print("\nChoose a valid action\n")
                if michelangelo.health <= 0:
                    print("Jack Sparrow won!")
                    break
                elif jack_sparrow.health <= 0:
                    print("Michelangelo won!")
                    break
                else:
                    print("Match Continues")
print("Game Over!")















