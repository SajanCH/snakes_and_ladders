from src.moving_entity import MovingEntity

class Board:

    def __init__(self, _dim: int) -> None:
        self.dimension = _dim
        self.moving_entities = {}
    

    def has_moving_entity(self, _pos: int) -> bool:
        return _pos in self.moving_entities
    

    def get_moving_entity(self, _pos: int) -> MovingEntity:
        if self.has_moving_entity:
            return self.moving_entities[_pos]
        else:
            print("There is no such entity.")


    def add_moving_entity(self, _entity: MovingEntity) -> None:
        key = _entity.get_action_position()
        self.moving_entities[key] = _entity


    def get_total_cells(self):
        return self.dimension ** 2
    

    def print_board(self) -> None:
        total_cells = self.dimension ** 2
        for i in range(total_cells, 0, -1):
            print('|' + str(i) + '\t', end='')

            if self.has_moving_entity(i):
                end_pos = self.moving_entities[i].get_id()
                print(end_pos, end='')

            print('|', end='')

            if i < total_cells and i % 10 == 0:
                print()
    

