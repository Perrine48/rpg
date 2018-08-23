#!/usr/bin/env python
# -- coding: UTF-8 --
class Character():
    def __init__(self, name, health, mana, power, xp):
        self.name = name
        self.health = health
        self.xp = xp
        self.power = power
        self.inventory = []
        self.mana = mana 
    def move(self):
        pass
    def attack(self):
        pass
    def pick(self):
        pass
    def throw(self):
        pass
    def use(self):
        pass

class Wizard(Character):
    def __init__(self, name):
        Character.__init__(self, name, 100, 100, 50, 0)
        self.spells = []

class Warrior(Character):
    def __init__(self, name, armor):
        Character.__init__(self, name, 200, 0, 300, 0)
        self.armor = armor
