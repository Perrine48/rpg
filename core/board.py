#!/usr/bin/env python
# -- coding: UTF-8 --

class Board():
    def __init__(self, nb_row, nb_col):
        self.grid = []
        for lig in range(nb_row):
            self.grid.append([])
            self.grid[lig].append([] * nb_col)

    def move(self, character, x, y):
        character.x = x
        character.y = y
        self.grid[x][y] = [character]
