from entities import Entity


class Item(Entity):
    def __init__(self, name, symbol, loc_i, loc_j, attack, defense, worth):
        super().__init__(name, symbol, loc_i, loc_j)
        self.attack = attack
        self.defense = defense
        self.worth = worth


class Treasure(Item):
    def __init__(self, loc_i, loc_j):
        super().__init__('treasure', '☆', loc_i, loc_j, 0, 0, worth=1)

# class TreasureHoard(Item):
#     def __init__(self, loc_i, loc_j, worth):
#         super().__init__('treasure hoard', ' ', loc_i, loc_j, 0, 0, worth=10)

# class Shield(Item):
#     def __init__(self, loc_i, loc_j, defense_modifier):
#         super().__init__('sword', '☨', loc_i, loc_j, 0, defense_modifier)


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