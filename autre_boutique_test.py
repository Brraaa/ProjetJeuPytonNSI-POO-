import pygame
from main import *
from player import Player
class Item:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def display_info(self):
        print(f"{self.name}: {self.description}, Prix: {self.price} XP")

'''
class Player:
    def __init__(self, name, gold):
        self.name = name
        self.gold = gold
        self.inventory = []

    def display_inventory(self):
        print(f"{self.name}'s Inventory:")
        for item in self.inventory:
            item.display_info()

    def buy_item(self, item):
        if self.gold >= item.price:
            self.gold -= item.price
            self.inventory.append(item)
            print(f"Vous avez acheté {item.name}. XP restant : {self.gold}")
        else:
            print("Pas assez d'XP pour acheter cet élément.")
'''
player = Player()

class Shop:
    def __init__(self):
        self.items_for_sale = []

    def display_items(self):
        print("Items à vendre:")
        for item in self.items_for_sale:
            item.display_info()

    def add_item(self, item):
        self.items_for_sale.append(item)


# Exemple d'utilisation
if __name__ == "__main__":
    sword = Item("Sword", "A sharp weapon", 10)
    potion = Item("Health Potion", "Restores health", 5)

    player = Player("Player1", 20)
    shop = Shop()

    shop.add_item(sword)
    shop.add_item(potion)

    shop.display_items()

    player.display_inventory()

    player.buy_item(sword)
    player.buy_item(potion)

    player.display_inventory()
