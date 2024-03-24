from src.moving_entity import MovingEntity

class Ladder(MovingEntity):

    def __init__(self, _start: int, _end: int) -> None:
        super(Ladder, self).__init__(_start, _end)


    def get_id(self) -> str:
        return 'L' + str(self.get_end_position)
    