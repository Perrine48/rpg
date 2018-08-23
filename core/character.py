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

    def attack(self, target):
        if target.health>=self.power :
            self.xp += target.power
        else :
            self.xp += 2
        target.health -= self.power

    def pick(self, item):
        self.inventory.append(item)

    def drop(self, item):
        self.inventory.remove(item)

    def use(self, item):
        if item in self.inventory :
            item.use(self)
            self.drop(item)
        else:
            raise

class Wizard(Character):
    def __init__(self, name):
        Character.__init__(self, name, 100, 100, 50, 0)
        self.spells = []

    def invoke(self, spell, target):
        if spell in self.inventory :
            target.health -= spell.damage
            self.use(spell)
        else:
            raise

class Warrior(Character):

    def __init__(self, name, armor):
        Character.__init__(self, name, 200, 0, 300, 0)
        self.armor = armor
