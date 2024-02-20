import random
import time
from abc import ABC, abstractmethod

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 120 
        self.inventory = set()
        self.tasks = []

    def add_to_inventory(self, item):
        self.inventory.add(item)

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

    def display_info(self):
        print(f"*** {self.name} ***")
        print(f"*** {self.description} ***")


class Character:
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

    def add_character(self, character: Character):
        pass

    def remove_character(self, character: Character):
        pass

class Forest(Location):
    def __init__(self):
        super().__init__(name="Enchanted Forest", description="Lush Green Forest Full of Magic")
        self.characters = []

    def get_challenge(self):
        print("Grishnook the goblin spots you from the treeline")
    
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
        print("There are luckily no enemies here, though it is very cold.")


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
    goblin1 = Goblin("Grishnook")
    goblin2 = Goblin("Snag")
    bandit = Bandit("Aragalt")
    archer = Archer("Hawkolas")

    forest = Forest()
    mountain = Mountain()
    ruin = Ruin()
    temple = Temple()

    locations = [forest, mountain, ruin, temple]
    available_locations = locations[:]

    artifact1 = Artifact("Orb of Truth", "A Mystical Orb That Reveals Hidden Secrets When Touched.")
    artifact2 = Artifact("Blade of Shadows", "A Dagger That Can Pierce Through Darkness. It is Able to Wound Even Paranormal and Magical Adversaries.")
    artifact3 = Artifact("Goblet of Eternal Youth", "A Magical Goblet Which Grants Immortality to Those Who Drink From it.")
    artifact4 = Artifact("Necklace of Invisibility", "A Necklace When Worn, Cloaks the Wearer From the Sight of Any Being.")

    print()
    print_slow("Welcome to 'The Quest of the Legendary Artifacts'")
    print_slow("Your Goal is to Recover Four Missing Legendary Artifacts in Different Locations")
    print()

    visited_locations = set()
    collected_artifacts = set()

    while len(visited_locations) < len(locations):
        chosen_location = input("Choose Which Location You Want To Explore: Forest | Mountain | Ruin | Temple: ").lower()
        print()


        if chosen_location == "forest" and forest not in visited_locations:
            visited_locations.add(forest)
            print()
            print_slow(f"*** LOCATION: {forest.name} ***")
            print_slow(f"*** DESCRIPTION: {forest.description} ***")
            print()
            print_slow("You come to a beautiful clearing. You hear some rustling in the distance.")
            print()
            forest.get_challenge()
            print_slow("He draws his sword and sprints towards you.")
            print()

            forest.add_character(goblin1)

            print()
            print_slow("""With less than a few feet remaining, three arrows impale the goblin""")
            print()
            forest.add_character(archer)
            print()
            archer.attack_player(goblin1)
            print()
            print_slow("An archer jumps down from a tree and gives you a nod.")
            print_slow("He tells you to stay safe and get some sword lessons.")

            print()
            print_slow("You continue your walk through the timber and notice a strange branch on a fir tree.")
            print_slow("You take a closer look and realize it's a dagger!")
            print()
            artifact2.display_info()
            print()
        
            while True:
                user_input_forest = input(f"Would you like to add The {artifact2.name} to your inventory? Yes | No : ").lower()
                print()

                if user_input_forest == "yes":
                    player.add_to_inventory(artifact2.name)
                    print_slow(f"{player.name} has obtained The Blade of Shadows!")
                    print("Player's Inventory:", player.inventory)
                    print()
                elif user_input_forest == "no":
                    print_slow("You leave the artifact and continue on your adventure.")
                else:
                    print_slow("Invalid Input. Please enter Yes | No : ")
                    continue
                break
                    

        if chosen_location == "mountain" and mountain not in visited_locations:
            visited_locations.add(mountain)
            print_slow(f"*** LOCATION: {mountain.name} ***")
            print_slow(f"*** DESCRIPTION: {mountain.description} ***")
            print()
            print_slow("""The high climb is refreshing, but fatigues you.""")
            print()
            mountain.get_challenge()
            print()
            print_slow("""You reach the summit, and there lies a spherical glass orb atop a flat boulder.""")
            print()
            artifact1.display_info()
            print()
        
            while True:
                user_input_mountain = input(f"Would you like to add The {artifact1.name} to your inventory? Yes | No : ").lower()
                print()

                if user_input_mountain == "yes":
                    player.add_to_inventory(artifact1.name)
                    print_slow(f"{player.name} has obtained The Orb of Truth!")
                    time.sleep(0.5)
                    print("Player's Inventory:", player.inventory)
                    print()
                elif user_input_mountain == "no":
                    print_slow("You leave the artifact and continue on your adventure.")
                else:
                    print_slow("Invalid Input. Please enter Yes | No : ")
                    continue
                break


        if chosen_location == "ruin" and ruin not in visited_locations:
            visited_locations.add(ruin)
            print()
            print_slow(f"*** LOCATION: {ruin.name} ***")
            print_slow(f"*** DESCRIPTION: {ruin.description} ***")
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
            artifact3.display_info()
            print()

            while True:
                user_input_ruin = input(f"Would you like to add the {artifact3.name} to your inventory? Yes | No : ").lower()
                print()

                if user_input_ruin == "yes":
                    player.add_to_inventory(artifact3.name)
                    print_slow(f"{player.name} has obtained The Goblet of Eternal Youth!")
                    time.sleep(0.5)
                    print("Player's Inventory:", player.inventory)
                    print()
                elif user_input_ruin == "no":
                    print_slow("You leave the artifact and continue on your adventure.")
                else:
                    print_slow("Invalid Input. Please enter Yes | No : ")
                    continue
                break


        if chosen_location == "temple" and temple not in visited_locations:
            visited_locations.add(temple)
            print()
            print_slow(f"*** LOCATION: {temple.name} ***")
            print_slow(f"*** DESCRIPTION: {temple.description} ***")    
            print()
            print_slow("You walk into the towering temple in awe.")
            print_slow("On the wall are strange petroglyphs, depicting goblins having dominion over the world.")
            print()
            print_slow(temple.get_challenge())
            print_slow("This time, you decide to handle it yourself.") 
            print()
            temple.add_character(goblin2)
            print()


            while player.health > 0 and not goblin2.defeated:
                action = input("Choose One! Attack | Retreat: ").lower()
                if action == "attack":
                    player.attack(goblin2)
                    if not goblin2.defeated and random.random() < 0.7:
                        goblin2.attack_player(player)
                elif action == "retreat":
                    print_slow("You decide the goblin looks too powerful and quickly run out of the Temple and into the trees")
                    break

            if player.health <= 0:
                print_slow("You have been defeated! Game Over.")
            elif not goblin2.defeated:
                print_slow("You retreat and do not obtain an Artifact ... You are a coward ...")
            else:
                print()
                print_slow("Congratulations! You defeated the goblin and obtained The Necklace of Invisibility.")
                print()
                artifact4.display_info()
                player.add_to_inventory("Necklace of Invisibility")
                print()
                time.sleep(0.05)
                print("Player's Inventory:", player.inventory)
                print()


    available_locations = [location for location in locations if location not in visited_locations]

    for artifact in [artifact1, artifact2, artifact3, artifact4]:
        if artifact.name in player.inventory:
            collected_artifacts.add(artifact)

    if len(collected_artifacts) == 4:
        print()
        print("Congratulations! You have collected all four Legendary Artifacts and won the game!")
    else:
        print()
        print("You have failed to collect all four Legendary Artifacts. Game over.")


if __name__ == "__main__":
    main()
