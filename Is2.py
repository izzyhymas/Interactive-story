from abc import ABC

class Player:
    def __init__(self):
    pass



class Artifacts:
    pass



class Location(ABC):
    pass




class Forrest(Location):
    pass




class Mountain(Location):
    pass



class Ruins(Location):
    pass



class Temple(Location):
    pass



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
    
    def cast_spell(self, player):
        damage = 35 # Unique ability: Wizard casts a powerful spell for fixed damage
        print(f"{self.name} casts a powerful spell on {player.name} for {damage} damage!")
        player.take_damage(damage)
        pass



class Goblin(Character):
    def __init__(self, name):
        super().__init__(name, health=55, attack=20)
    
    def steal_gold(self, player):
        gold_stolen = 10 # Unique ability: Goblin steals gold from the player
        print(f"{self.name} steals {gold_stolen} gold from {player.name}!")

    #implement gold logic later here
    pass



class Ranger(Character):
    def __init__(self, name):
        super().__init__(name, health=70, attack=25)
    
    def throw_knife(self, player):
        damage = 35 # Unique ability: Ranger throws a knife for fixed damage
        print(f"{self.name} throws a knife at {player.name} for {damage} damage!")
        player.take_damage(damage)
    pass


class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=65, attack=25)
    
    def rapid_fire(self, player):
        damage = 15 # Unique ability: Archer rapidly fires arrows for less damage but multiple attacks
        print(f"{self.name} rapidly fires arrows at {player.name}")
        for _ in range (3):
            player.take_damage(damage)

    pass


wizard = Wizard("Dumbledalf")
goblin = Goblin("Grishnook")
ranger = Ranger("Aragalt")
archer = Archer("Hawkolas")

player = Player("Player")

wizard.cast_spell(player)
goblin.steal_gold(player)
ranger.throw_knife(player)
archer.rapid_fire(player)
















#Inventory(set)




#Clues(list)


#Tasks(list)


