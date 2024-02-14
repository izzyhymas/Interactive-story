from abc import ABC, abstractmethod

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100  # Initial health value
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


player = Player("Player")

print("Player Health:", player.health)  # Print initial health value

# Add items to inventory
player.add_to_inventory("Sword")
player.add_to_inventory("Shield")
print("Inventory:", player.inventory)


# Add tasks
player.add_task("")
player.add_task("")
print("Tasks:", player.tasks)


class Artifact:
    def __init__(self, name, description):
        self.name = name
        self.description = description


artifact1 = Artifact("Orb of Truth", "A mystical orb that reveals hidden secrets when touched.")
artifact2 = Artifact("Blade of Shadows", "A dagger that can pierce through darkness, able to wound even paranormal and magical adversaries.")
artifact3 = Artifact("Goblet of Eternal Youth", "A magical goblet which grants immortality to those who drink from it.")
artifact4 = Artifact("Necklace of Invisibility", "A necklace when worn, cloaks the wearer from the sight of any being.")

print("Artifact 1:", artifact1.name)
print("Description:", artifact1.description)

print("Artifact 2:", artifact2.name)
print("Description:", artifact2.description)

print("Artifact 3:", artifact3.name)
print("Description:", artifact3.description)

print("Artifact 4:", artifact4.name)
print("Description:", artifact4.description)


class Location(ABC):
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    @abstractmethod
    def get_challenge(self):
        pass

    @abstractmethod
    def add_character(self):
        pass

    @abstractmethod
    def remove_character(self):
        pass


class Forest(Location):
    def __init__(self):
        super().__init__(name="Enchanted Forest", description="Lush Green Forest Full of Magic")

    def get_challenge(self):
        return "You See a goblin in the clearing ahead looting a corpse."

    def add_character(self):
        return super().add_character()

    def remove_character(self):
        return super().remove_character()


class Mountain(Location):
    def __init__(self):
        super().__init__(name="Misty Mountain", description="Massive Mountain Covered in Mist")

    def get_challenge(self):
        return "You grow weary as you approach the summit."

    def add_character(self):
        return super().add_character()

    def remove_character(self):
        return super().remove_character()


class Ruins(Location):
    def __init__(self):
        super().__init__(name="Ancient Ruins", description="Ancient City of Stone which crumbles to the touch")

    def get_challenge(self):
        return """You hear a scraping sound. You move towards the cracked building it's coming from.
        Suddenly a bandit emerges from the threshold."""

    def add_character(self):
        return super().add_character()

    def remove_character(self):
        return super().remove_character()


class Temple(Location):
    def __init__(self):
        super().__init__(name="Sacred Temple", description="Beautiful Old Temple Surrounded by Trees")

    def get_challenge(self):
        return "You enter the temple and it's empty."

    def add_character(self):
        return super().add_character()

    def remove_character(self):
        return super().remove_character()


def main():
    forest = Forest()
    mountain = Mountain()
    ruin = Ruins()
    temple = Temple()

    locations = [forest, mountain, ruin, temple]

    print()
    print("Welcome to 'The Quest of the Legendary Artifacts'")
    print("Your Goal is to Recover the Four Legendary Artifacts in Different Locations")
    print()
    chosen_location = input("Choose Which Location You Want to Explore First: Forest | Mountain | Ruin | Temple: ")
    print()

    if chosen_location.lower() == "forest":
        print(f"You Chose The {forest.name}. It is a {forest.description} ")
    elif chosen_location.lower() == "mountain":
        print(f"You Chose The {mountain.name}. It is a {mountain.description} ")
    elif chosen_location.lower() == "ruin":
        print(f"You Chose The {ruin.name}. It is a {ruin.description} ")
    elif chosen_location.lower() == "temple":
        print(f"You Chose The {temple.name}. It is a {temple.description} ")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()


class Character(ABC):
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def attack_player(self, player):
        damage = self.attack
        print(f"{self.name} attacks {player.name} for {damage} damage!")
        player.take_damage(damage)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has been defeated!")
        else:
            print(f"{self.name} has {self.health} health remaining.")


class Wizard(Character):
    def __init__(self, name):
        super().__init__(name, health=80, attack=25)

    def cast_spell(self, bandit):
        damage = 35  # Unique ability: Wizard casts a powerful spell for fixed damage
        print(f"{self.name} casts a powerful spell on {bandit.name} for {damage} damage!")
        bandit.take_damage(damage)
        pass


class Goblin(Character):
    def __init__(self, name):
        super().__init__(name, health=55, attack=20)

    def attack_player(self, player):
        damage = self.attack
        print(f"{self.name} attacks {player.name} for {damage} damage!")
        player.take_damage(damage)
    pass


class Bandit(Character):
    def __init__(self, name):
        super().__init__(name, health=70, attack=25)

    def throw_knife(self, player):
        damage = 35  # Unique ability: Bandit throws a knife for fixed damage
        print(f"{self.name} throws a knife at {player.name} for {damage} damage!")
        player.take_damage(damage)
    pass


class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=65, attack=25)

    def rapid_fire(self, goblin):
        damage = 15  # Unique ability: Archer rapidly fires arrows for less damage but multiple attacks
        print(f"{self.name} rapidly fires arrows at {goblin.name}")
        for _ in range(3):
            goblin.take_damage(damage)
    pass


# example use

wizard = Wizard("Dumbledalf")
goblin = Goblin("Grishnook")
bandit = Bandit("Aragalt")
archer = Archer("Hawkolas")
player = Player("Player")


# Forest quest
forest = Forest("Enchanted Forest", "Lush Green Forest Full of Magic.")
forest.add_character(archer)
forest.add_character(goblin)

# Goblin charges player
print("""You come to a clearing and to your surprise, a goblin spots you 
      from the treeline. He draws his sword and sprints towards you.""")

# Archer saves the player
archer.rapid_fire(goblin)
print("""With less than a few feet remaining, three arrows impale the goblin""")
print("""An archer jumps down from a tree and gives you a nod. He tells you to 
      stay safe and get some sword lessons.""")

# Add the blade of shadows to forest
print("""You continue your walk through the timber and notice a strange branch
      on a fir tree. You take a closer look and realize it's a dagger!""")
print(artifact2)

# Add artifact to inventory
player.add_to_inventory(artifact2.name)
print(f"{player.name} has obtained the blade of shadows!")

# Print inventory
print("Player's Inventory:", player.inventory)

# Transition to mountain
mountain = Mountain("Misty Mountains", "Massive Mountains Covered in Mist.")
print("The high climb is refreshing, but fatigues you. ")

# Add the orb to mountain
print("""You reach the summit, and there lies a spherical glass orb atop a flat boulder.""")
print(artifact1.name)
print(artifact1.description)

# Add artifact to inventory
player.add_to_inventory(artifact1.name)
print(f"{player.name} has obtained the orb of truth!")

# Print inventory
print("Player's Inventory:", player.inventory)

# Transition to ruins
ruins = Ruins()
ruins.add_character(wizard)
ruins.add_character(bandit)
print(ruins.name, ruins.description)

# Character getting attacked by bandit
ruins.get_challenge()

# Wizard saves the character
wizard.cast_spell(bandit)
print("Suddenly, a wizard cloaked in grey steps in front of you and casts a spell on the charging bandit.")
print("He tells you to tread lightly in these ruins, and vanishes with a poof into a cloud of smoke.")
print("As the smoke cloud dissapears, you notice a strange object left where the wizard was standing.")
print(artifact3.name)
print(artifact3.description)

# Add artifact to inventory
player.add_to_inventory(artifact3)
print(f"{player.name} has obtained the Goblet of Eternal youth!")
print(player.inventory)

#Transition to temple
temple = Temple()
print(f"You chose the {temple.name}. It is a {temple.description}.")
print(temple.get_challenge())
temple.add_character(goblin)



#Setting the scene
print("""You walk into the towering temple in awe. On the wall are strange petroglyphs, depicting goblins
      having dominion over the world""")
print("""You hear a snarl behind you. It's another Goblin.""")
print("This time, you decide to handle it yourself.")


# Player defends against the goblin
while player.health > 0 and temple.goblin.health > 0:
    player.attack(temple.goblin)
    if temple.goblin.health > 0:
        temple.goblin.attack_player(player)

if player.health <= 0:
        print("You have been defeated! Game Over.")
else:
        print("Congratulations! You defeated the goblin and obtained the Necklace of Invisibility.")
        player.add_to_inventory("Necklace of Invisibility")

    # Other parts of the main function...


if __name__ == "__main__":
    main()