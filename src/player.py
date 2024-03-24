class Player:

    def __init__(self, _name: str) -> None:
        self.name = _name
        self.position = 1
    

    def set_position(self, pos: int) -> None:
        self.position = pos

    
    def get_position(self) -> int:
        return self.position
    
    def get_name(self) -> str:
        return self.name
    