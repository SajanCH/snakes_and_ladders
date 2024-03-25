from src.moving_entity import MovingEntity

class Snake(MovingEntity):

    def __init__(self, _start: int, _end: int) -> None:
        super(Snake, self).__init__(_start, _end)


    def get_id(self) -> str:
        return 'S' + str(self.get_end_position())
    