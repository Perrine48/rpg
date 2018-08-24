#!/usr/bin/env python
# -- coding: UTF-8 --

class Item():
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

class Spell(Item):
    def __init__(self, name, weight, cost, damage):
        Item.__init__(self, name, weight)
        self.cost = cost
        self.damage = damage

    def use(self, character):
        if character.mana >= self.cost:
            character.mana -= self.cost

class Apple(Item):
    def __init__(self, weight, gain):
        Item.__init__(self, "Apple", weight)
        self.gain = gain
    def use(self, character):
        character.health += self.gain
