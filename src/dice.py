from random import randint

class Dice:

    def __init__(self, _val: int) -> None:
        self.max_value = _val

    
    def roll(self) -> int:
        return randint(1, self.max_value + 1)
    