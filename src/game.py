from src.board import Board
from src.dice import Dice
from src.player import Player

from collections import deque

class Game:

    def __init__(self, _board: Board, _dice: Dice) -> None:
        self.board = _board
        self.dice = _dice
        self.players = deque()


    def add_player(self, _player: Player) -> None:
        self.players.append(_player)


    def make_a_move(self, _player: Player) -> None:
        print()
        print(_player.get_name() + "'s turn.")
        print("Press anything to roll dice")

        dummy = input()

        player_position = _player.get_position()

        roll_value = self.dice.roll()

        target_position = player_position + roll_value \
            if player_position + roll_value <= self.board.get_total_cells() \
            else player_position

        if self.board.has_moving_entity(target_position):
            target_position = self.board.get_moving_entity(target_position).get_end_position()
        
        _player.set_position(target_position)


    def start_game(self) -> None:
        self.board.print_board()

        while len(self.players) > 1:
            _player = self.players.popleft()
            self.make_a_move(_player)

            if _player.get_position() == self.board.get_total_cells():
                print(_player.get_name() + "has completed the game!!")
            else:
                self.players.append(_player)
                