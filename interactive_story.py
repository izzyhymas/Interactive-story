import random
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
        super().__init__(name, health=80, attack=25)

    def cast_spell(self, bandit):
        damage = 35 
        print(f"{self.name} casts a powerful spell on {bandit.name} for {damage} damage!")
        bandit.take_damage(damage)


class Goblin(Character):
    def __init__(self, name):
        super().__init__(name, health=55, attack=20)


class Bandit(Character):
    def __init__(self, name):
        super().__init__(name, health=70, attack=25)


class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=65, attack=25)


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

    def get_challenge(self):
        return "You See a Wizard in the Distance..."

    def add_character(self, character: Character):
        print(f"{character.name} appears in the Enchanted Forest with {character.health} health")

    def remove_character(self, character: Character):
        print(f"{character.name} removed from Enchanted Forest")


class Mountain(Location):
    def __init__(self):
        super().__init__(name="Misty Mountains", description="Massive Mountains Covered in Mist")

    def get_challenge(self):
        return "You See a Troll in the Distance"

    def add_character(self, character: Character):
        print(f"{character.name} appears in the Misty Mountains with {character.health} health")

    def remove_character(self, character: Character):
        print(f"{character.name} removed from Misty Mountains")


class Ruin(Location):
    def __init__(self):
        super().__init__(name="Ancient Ruin", description="Very Old Ruins That Crumble to the Touch")

    def get_challenge(self):
        return "You see a ... in the Distance"

    def add_character(self, character: Character):
        print(f"{character.name} appears in Ancient Ruin with {character.health} health")

    def remove_character(self, character: Character):
        print(f"{character.name} removed from Ancient Ruin")


class Temple(Location):
    def __init__(self):
        super().__init__(name="Sacred Temple", description="Beautiful Old Temple Surronded by Trees")

    def get_challenge(self):
        return "You See a Bandit in the Distance"

    def add_character(self, character: Character):
        print(f"{character.name} appears in Sacred Temple with {character.health} health")

    def remove_character(self, character: Character):
        print(f"{character.name} removed from Sacred Temple")


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
    print("Welcome to 'The Quest of the Legendary Artefact'")
    print("Your Goal is to Recover Four Missing Legendary Artefacts in Different Locations")
    print()

    chosen_location = input("Choose Which Location You Want to Explore First: Forest | Mountain | Ruin | Temple: ")
    print()

    chosen_location = chosen_location.lower()

    if chosen_location == "forest":
        print(f"You Chose The {forest.name}. It is a {forest.description} ")
    elif chosen_location == "mountain":
        print(f"You Chose The {mountain.name}. It is a {mountain.description} ")
    elif chosen_location == "ruin":
        print(f"You Chose The {ruin.name}. It is a {ruin.description} ")
    elif chosen_location == "temple":
        print(f"You Chose The {temple.name}. It is a {temple.description} ")
    else:
        print("Invalid choice.")

    if chosen_location == "forest":
        print()
        forest.add_character(archer)
        forest.add_character(goblin)

        print()
        print("""You come to a clearing and to your surprise, a goblin spots you 
              from the treeline. He draws his sword and sprints towards you.""")

        archer.attack(goblin)

        print("""With less than a few feet remaining, three arrows impale the goblin""")
        print("""An archer jumps down from a tree and gives you a nod. He tells you to 
              stay safe and get some sword lessons.""")

        print()
        print("""You continue your walk through the timber and notice a strange branch
              on a fir tree. You take a closer look and realize it's a dagger!""")
        print(f"*** {artifact2.name} ***")

        player.add_to_inventory(artifact2.name)
        print(f"{player.name} has obtained the blade of shadows!")

        print("Player's Inventory:", player.inventory)

    if chosen_location == "mountain":
        print("""The high climb is refreshing, but fatigues you.""")
        print("""You reach the summit, and there lies a spherical glass orb atop a flat boulder.""")
        print()
        print(f"*** {artifact1.name} ***")
        
        player.add_to_inventory(artifact1.name)
        print(f"{player.name} has obtained the orb of truth!")

        print("Player's Inventory:", player.inventory)

    if chosen_location == "ruin":
        ruin.add_character(wizard)
        ruin.add_character(bandit)

        print(ruin.name, ruin.description)

        print(wizard.get_challenge())

        wizard.cast_spell(bandit)
        print("Suddenly, a wizard cloaked in grey steps in front of you and casts a spell on the charging bandit.")
        print("He tells you to tread lightly in these ruins, and vanishes with a poof into a cloud of smoke.")
        print("As the smoke cloud disappears, you notice a strange object left where the wizard was standing.")
        print()
        print(f"*** {artifact3.name}     ***")

        player.add_to_inventory(artifact3.name)
        print(f"{player.name} has obtained the Goblet of Eternal youth!")
        print("Player's Inventory:", player.inventory)

    if chosen_location == "temple":
        temple.add_character(goblin)

        print(f"You chose the {temple.name}. It is a {temple.description}.")
        print(temple.get_challenge())

        print("""You walk into the towering temple in awe. On the wall are strange petroglyphs, depicting goblins
              having dominion over the world""")
        print("""You hear a snarl behind you. It's another Goblin.""")
        print("This time, you decide to handle it yourself.")

        while player.health > 0 and not goblin.defeated:
            action = input("Choose One: Attack | Retreat ").lower()
            if action == "attack":
                player.attack(goblin)
            if not goblin.defeated:
                if random.random() < 0.7:
                    goblin.attack_player(player)
            elif action == "retreat":
                print("You Retreat")
                break

        if player.health <= 0:
            print("You have been defeated! Game Over.")
        else:
            print("Congratulations! You defeated the goblin and obtained the Necklace of Invisibility.")
            player.add_to_inventory("Necklace of Invisibility")
            print("Player's Inventory:", player.inventory)



if __name__ == "__main__":
    main()
