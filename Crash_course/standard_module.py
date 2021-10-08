import random as r


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self, times):
        for i in range(times):
            print(r.randint(1, self.sides))


die6 = Die()
die10 = Die(10)
die20 = Die(20)
# die6.roll_die(10)
# die10.roll_die(10)
die20.roll_die(20)
