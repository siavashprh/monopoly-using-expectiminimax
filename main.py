import random

'''
the Player class.
the Player class has the id, token, balance, position and properties attributes.
the id and token attributes are self-explanatory.
the balance attribute represents the amount of money the player has. which is set to 1500 at the start of the game.
the position attribute represents the locatio nof the player on the board.
the properties attributes is the list of properties owned by the player. it is a list containing objects of Property class.
the pay and receive methods decrease and increase the player balance respectively.
'''
class Player:
    def __init__(self, id, token, balance=1500, position=0, properties=[]):
        self.id = id
        self.token = token
        self.balance = balance
        self.position = position
        self.properties = properties

    def __str__(self):
        return f"Player {self.id} ({self.token}): balance=${self.balance}, position={self.position}, properties={self.properties}"
        
    def add_property(self, property):
        self.properties.append(property)
    
    def remove_property(self, property):
        self.properties.remove(property)
    
    def pay(self, amount):
        self.balance -= amount
    
    def receive(self, amount):
        self.balance += amount

class Property:
    def __init__(self, name, value, owner):
        self.name = name
        self.value = value
        self.owner = owner

# the Board class
# the Board class has the players and properties attributes
class Board:
    def __init__(self, players, properties):
        self.players = players
        self.properties = properties
    
    def __str__(self):
        pass

    def move_player(self, player, steps):
        pass

class Dice:
    def __init__(self):
        pass

    def roll(self):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        return dice1 + dice2

class Game:
    def __init__(self, players, properties):
        self.board = Board(players, properties)
        self.dice = Dice()