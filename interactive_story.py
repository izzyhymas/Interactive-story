from abc import ABC, abstractmethod

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

    def remove_character(self):
        pass

class Forest(Location):
    def __init__(self):
        super().__init__(name="Enchanted Forest", description="Lush Green Forest Full of Magic")

    def get_challenge(self):
        return "You See a Wizard in the Distance..."
    
    def add_character(self):
        return super().add_character()
    
    def remove_character(self):
        return super().remove_character()

class Mountain(Location):
    def __init__(self):
        super().__init__(name="Misty Mountains", description="Massive Mountains Covered in Mist")

    def get_challenge(self):
        return "You See a Troll in the Distance"
    
    def add_character(self):
        return super().add_character()
    
    def remove_character(self):
        return super().remove_character()

class Ruin(Location):
    def __init__(self):
        super().__init__(name="Ancient Ruin", description="Very Old Ruins That Crumble to the Touch")

    def get_challenge(self):
        return "You see a ... in the Distance"
    
    def add_character(self):
        return super().add_character()
    
    def remove_character(self):
        return super().remove_character()
    
class Temple(Location):
    def __init__(self):
        super().__init__(name="Sacred Temple", description="Beautiful Old Temple Surronded by Trees")

    def get_challenge(self):
        return "You See a Bandit in the Distance"
    
    def add_character(self):
        return super().add_character()
    
    def remove_character(self):
        return super().remove_character()
    
    
def main():

    forest = Forest()
    mountain = Mountain()
    ruin = Ruin()
    temple = Temple()

    locations = [forest, mountain, ruin, temple]


    print()
    print("Welcome to 'The Quest of the Legendary Artefact'")
    print("Your Goal is to Recover the Four Pieces of the Missing Legendary Artefact in Different Locations")
    print()
    input("Choose Which Location You Want to Explore First: Forest|Mountain|Ruin|Temple: ")
    print()
    
    def get_location(self):
        if get_location == forest:
            print(f"You Chose The{forest.name}. It is a {forest.description} ")
            
if __name__ == "__main__":
    main()

