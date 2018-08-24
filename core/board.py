#!/usr/bin/env python
# -- coding: UTF-8 --
class Board():
    def __init__(self, nb_row, nb_col):
        self.grid = []
        for ligne in range(nb_row):
            self.grid.append([])
            for col in range(nb_col):
                self.grid[ligne].append([])

    def move(self, character, x, y):
        # if any(character in ligne for ligne in self.grid):
        # for ligne in range(len(self.grid)):
        if character.x != None and character.y != None:
            self.grid[character.x][character.y].remove(character)

        character.x = x
        character.y = y
        self.grid[x][y] = [character]
