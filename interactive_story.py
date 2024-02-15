import random
import time
from abc import ABC, abstractmethod

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100 
        self.inventory = set()
        self.tasks = []

    def add_to_inventory(self, item):
        self.inventory.add(item)

    def add_task(self, task):
        self.tasks.append(task)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has been defeated!")
        else:
            print(f"{self.name} has {self.health} health remaining.")

    def attack(self, character):
        damage = 10 
        print(f"{self.name} attacks {character.name} for {damage} damage!")
        character.take_damage(damage)


class Artifact:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Character(ABC):
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        self.defeated = False

    def attack_player(self, player):
        damage = self.attack
        print(f"{self.name} attacks {player.name} for {damage} damage!")
        player.take_damage(damage)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.defeated = True
            print(f"{self.name} has been defeated!")
        else:
            print(f"{self.name} has {self.health} health remaining.")


class Wizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack=70)

    def get_challenge(self):
        return "You see a powerful wizard in the distance"

    def cast_spell(self, character):
        damage = 70
        print(f"{self.name} casts a powerful spell on {character.name} for {damage} damage!")
        character.take_damage(damage)


class Goblin(Character):
    def __init__(self, name):
        super().__init__(name, health=55, attack=20)


class Bandit(Character):
    def __init__(self, name):
        super().__init__(name, health=70, attack=25)


class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=65, attack=55)


class Location(ABC):
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    @abstractmethod
    def get_challenge(self):
        pass

    @abstractmethod
    def add_character(self, character: Character):
        pass

    @abstractmethod
    def remove_character(self, character: Character):
        pass
class Forest(Location):
    def __init__(self):
        super().__init__(name="Enchanted Forest", description="Lush Green Forest Full of Magic")
        self.characters = []

    def get_challenge(self):
        return super().get_challenge()
    
    def add_character(self, character: Character):
        self.characters.append(character)
        print(f"{character.name} appears in the Enchanted Forest with {character.health} health")

    def remove_character(self, character: Character):
        self.characters.remove(character)
        print(f"{character.name} removed from Enchanted Forest")


class Mountain(Location):
    def __init__(self):
        super().__init__(name="Misty Mountain", description="Massive Mountain Covered in Mist")

    def get_challenge(self):
        return "You See a Troll in the Distance"

    def add_character(self, character: Character):
        print(f"{character.name} appears in the Misty Mountains with {character.health} health")

    def remove_character(self, character: Character):
        print(f"{character.name} removed from Misty Mountains")


class Ruin(Location):
    def __init__(self):
        super().__init__(name="Ancient Ruin", description="Very Old Ruin That Crumbles to the Touch")

    def get_challenge(self):
        return "You see a bandit appear from around the corner. He sees you and starts charging towards you"
    

    def add_character(self, character: Character):
        print(f"{character.name} appears in Ancient Ruin with {character.health} health")

    def remove_character(self, character: Character):
        print(f"{character.name} removed from Ancient Ruin")


class Temple(Location):
    def __init__(self):
        super().__init__(name="Sacred Temple", description="Beautiful Old Temple Surronded by Trees")

    def get_challenge(self):
        return "You See a Goblin Grab an Artifact in the Distance. He Spots You!"

    def add_character(self, character: Character):
        print(f"{character.name} appears in Sacred Temple with {character.health} health")

    def remove_character(self, character: Character):
        print(f"{character.name} removed from Sacred Temple")

def print_slow(text, delay=0.04):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


def main():
    player = Player("Player")
    wizard = Wizard("Dumbledalf")
    goblin = Goblin("Grishnook")
    bandit = Bandit("Aragalt")
    archer = Archer("Hawkolas")

    forest = Forest()
    mountain = Mountain()
    ruin = Ruin()
    temple = Temple()

    locations = [forest, mountain, ruin, temple]

    artifact1 = Artifact("Orb of Truth", "A mystical orb that reveals hidden secrets when touched.")
    artifact2 = Artifact("Blade of Shadows", "A dagger that can pierce through darkness, able to wound even paranormal and magical adversaries.")
    artifact3 = Artifact("Goblet of Eternal Youth", "A magical goblet which grants immortality to those who drink from it.")
    artifact4 = Artifact("Necklace of Invisibility", "A necklace when worn, cloaks the wearer from the sight of any being.")

    print()
    print_slow("Welcome to 'The Quest of the Legendary Artefact'")
    print_slow("Your Goal is to Recover Four Missing Legendary Artefacts in Different Locations")
    print()

    time.sleep(0.05)
    chosen_location = input("Choose Which Location You Want to Explore First: Forest | Mountain | Ruin | Temple: ")
    print()

    chosen_location = chosen_location.lower()

    if chosen_location == "forest":
        print_slow(f"You Chose The {forest.name}. It is a {forest.description} ")
    elif chosen_location == "mountain":
        print_slow(f"You Chose The {mountain.name}. It is a {mountain.description} ")
    elif chosen_location == "ruin":
        print_slow(f"You Chose The {ruin.name}. It is a {ruin.description} ")
    elif chosen_location == "temple":
        print_slow(f"You Chose The {temple.name}. It is a {temple.description} ")
    else:
        print_slow("Invalid choice.")

    if chosen_location == "forest":
        print()
        print_slow("You come to a clearing and to your surprise, Grishnook the goblin spots you from the treeline.")
        print_slow("He draws his sword and sprints towards you.")
        print()

        forest.add_character(goblin)

        print()
        print_slow("""With less than a few feet remaining, three arrows impale the goblin""")
        print()
        forest.add_character(archer)
        print()
        archer.attack_player(goblin)
        print()
        print_slow("An archer jumps down from a tree and gives you a nod.")
        print_slow("He tells you to stay safe and get some sword lessons.")

        print()
        print_slow("You continue your walk through the timber and notice a strange branch on a fir tree.")
        print_slow("You take a closer look and realize it's a dagger!")
        print()
        print_slow(f"*** {artifact2.name} ***")
        print()
        
        user_input_forest = input(f"Would you like to add the {artifact2.name} to your inventory? Yes | No : ").lower()

        if user_input_forest == "yes":
            player.add_to_inventory(artifact2.name)
            print_slow(f"{player.name} has obtained the blade of shadows!")
            print("Player's Inventory:", player.inventory)
        elif user_input_forest == "no":
            print_slow("You leave the artifact and continue on your adventure.")
        else:
            print_slow("Invalid Input. Please enter Yes | No : ")


    if chosen_location == "mountain":
        print_slow("""The high climb is refreshing, but fatigues you.""")
        print()
        print_slow("""You reach the summit, and there lies a spherical glass orb atop a flat boulder.""")
        print()
        print_slow(f"*** {artifact1.name} ***")
        
        user_input_mountain = input(f"Would you like to add the {artifact1.name} to your inventory? Yes | No : ").lower()
        if user_input_mountain == "yes":
            player.add_to_inventory(artifact1.name)
            print_slow(f"{player.name} has obtained the orb of truth!")
            print()
            time.sleep(0.5)
            print("Player's Inventory:", player.inventory)
        elif user_input_mountain == "no":
            print_slow("You leave the artifact and continue on your adventure.")
        else:
            print_slow("Invalid Input. Please enter Yes | No : ")


    if chosen_location == "ruin":
        print()
        print_slow(ruin.get_challenge())
        ruin.add_character(bandit)
        print()

        print_slow("Suddenly, a wizard cloaked in grey steps in front of you and casts a spell on the charging bandit.")
        ruin.add_character(wizard)
        print()
        wizard.cast_spell(bandit)
        print()
        print_slow("He tells you to tread lightly in these ruins, and vanishes with a poof into a cloud of smoke.")
        print_slow("As the smoke cloud disappears, you notice a strange object left where the wizard was standing.")
        print()
        print_slow(f"*** {artifact3.name} ***")
        print()

        user_input_ruin = input(f"Would you like to add the {artifact3.name} to your inventory? Yes | No : ").lower()
        if user_input_ruin == "yes":
            player.add_to_inventory(artifact3.name)
            print_slow(f"{player.name} has obtained The Goblet of Eternal Youth!")
            print()
            time.sleep(0.5)
            print("Player's Inventory:", player.inventory)
        elif user_input_ruin == "no":
            print_slow("You leave the artifact and continue on your adventure.")
        else:
            print_slow("Invalid Input. Please enter Yes | No : ")

    if chosen_location == "temple":
        print()
        print_slow("You walk into the towering temple in awe.")
        print_slow("On the wall are strange petroglyphs, depicting goblins having dominion over the world.")
        print()
        print_slow(temple.get_challenge())
        print_slow("This time, you decide to handle it yourself.") 
        print()
        temple.add_character(goblin)
        print()


        while player.health > 0 and not goblin.defeated:
            action = input("Choose One! Attack | Retreat: ").lower()
            if action == "attack":
                player.attack(goblin)
                if not goblin.defeated and random.random() < 0.7:
                    goblin.attack_player(player)
            elif action == "retreat":
                print_slow("You decide the goblin looks too powerful and quickly run out of the Temple and into the trees")
                break

        if player.health <= 0:
            print_slow("You have been defeated! Game Over.")
        elif not goblin.defeated:
            print_slow("You retreat and do not obtain an Artifact ... You are a coward ...")
        else:
            print()
            print_slow("Congratulations! You defeated the goblin and obtained the Necklace of Invisibility.")
            player.add_to_inventory("Necklace of Invisibility")
            print()
            time.sleep(0.05)
            print("Player's Inventory:", player.inventory)



if __name__ == "__main__":
    main()
