from src.game.entities import Team, Monkey, Queen
from src.game.board import Board
from src.game.geo import Vec2I
from src.game.command import Command
import random

"""
Code your AI in this file.
"""

# Define your persistent variables here


def make_play(board, your_team, last_move):
    """

    determiner les coups valides:
    1. coup oblique/horizontal/vertical (deja fait)
    2. si reine, coup qui ne la met pas en danger

    determiner le score de la position dans le plateau:
    - nombre de coups possibles pour la reine
    - nombre de bebes singes
    - /!\ si possibilite de capturer la reine, score 100000000

    :param board:
    :param your_team:
    :param last_move:
    :return:

    """

    depth = 1

    all_moves = board.get_legal_moves(your_team)
    best_move = all_moves[0]
    for i in range(depth):
        selected_move = all_moves[i]
        new_board = board.copy_state()
        new_board.play_command(Command(selected_move[0], selected_move[1]))

        black_number, white_number = 0, 0
        for entity in new_board.get_entities():
            team = entity.get_team()
            if team == Team.WHITE:
                white_number += 1
            else:
                black_number += 1

        best_move = selected_move

    return best_move
