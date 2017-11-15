'''
visible treasure: collect treasure

invisible enemies: do battle (how?) rock paper scissors
    if lose: lose health or treasure
    if win: defeat enemy, gain random treasure?
    if tie: display enemy, get half treasure


invisible health bonus

invisible bonus treasure





collect all visible treasure to win
lose if all health gone

'''

import random

class Entity:
    def __init__(self, name, symbol, loc_i, loc_j):
        self.name = name
        self.symbol = symbol
        self.loc_i = loc_i
        self.loc_j = loc_j


class LivingEntity(Entity):
    def __init__(self, name, symbol, loc_i, loc_j, health):
        super().__init__(name, symbol, loc_i, loc_j)
        self.health = health
        # self.attack = attack
        # self.defense = defense
        self.inventory = []


class Player(LivingEntity):
    def __init__(self, loc_i, loc_j):
        super().__init__('Player', '§', loc_i, loc_j, health=10)

    def fight(self, enemy):
        pass


class Knight(LivingEntity):
    def __init__(self, loc_i, loc_j):
        super().__init__('Knight', ' ', loc_i, loc_j, health=random.randint(1, 10))
        # when I want to print knight symbol: ☩

