from src.snake import Snake
from src.ladder import Ladder
from src.board import Board
from src.dice import Dice
from src.game import Game
from src.player import Player

def main():
    snake1 = Snake(12, 28)
    snake2 = Snake(34, 78)
    snake3 = Snake(6, 69)
    snake4 = Snake(65, 84)

    ladder1 = Ladder(24, 56)
    ladder2 = Ladder(43, 83)
    ladder3 = Ladder(3, 31)
    ladder4 = Ladder(72, 91)

    board = Board(10)
    board.add_moving_entity(snake1)
    board.add_moving_entity(snake2)
    board.add_moving_entity(snake3)
    board.add_moving_entity(snake4)
    
    board.add_moving_entity(ladder1)
    board.add_moving_entity(ladder2)
    board.add_moving_entity(ladder3)
    board.add_moving_entity(ladder4)

    dice = Dice(6)

    game = Game(board, dice)

    player1_name = input("Player 1 name:")
    player2_name = input("Player 2 name: ")

    player1 = Player(player1_name)
    player2 = Player(player2_name)

    game.add_player(player1)
    game.add_player(player2)

    game.start_game()


if __name__ == '__main__':
    main()
