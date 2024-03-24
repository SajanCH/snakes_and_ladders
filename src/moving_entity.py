class MovingEntity:

    def __init__(self, _start: int, _end: int) -> None:
        self.start = _start
        self.end = _end

    
    def get_end_position(self) -> int:
        return self.end
    

    def get_action_position(self) -> int:
        return self.start

