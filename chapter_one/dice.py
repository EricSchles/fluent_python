import collections

Dice = collections.namedtuple('Dice', ['side'])


class PairOfDice:
    dice_sides = [n for n in range(1, 7)]

    def __init__(self):
        tmp = []
        for first_dice in self.dice_sides:
            for second_dice in self.dice_sides:
                tmp.append((Dice(first_dice), Dice(second_dice)))
        self._dice = tmp

    def __len__(self):
        return len(self._dice)

    def __getitem__(self, position):
        return self._dice[position]
