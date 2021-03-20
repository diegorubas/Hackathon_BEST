from src.game.entities import Team, Monkey, Queen
from src.game.board import Board
from src.game.geo import Vec2I
from src.game.command import Command
import random

"""
Code your AI in this file.
"""

# Define your persistent variables here

depth = 1
infinity = 10000
alpha = -infinity
beta = infinity


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

    all_moves = board.get_legal_moves(your_team)
    best_move = all_moves[0]
    if your_team == Team.WHITE:
        best_val = -infinity
        for current_move in all_moves:
            new_board = board.copy_state()
            new_board.play_command(Command(current_move[0], current_move[1]))
            val = minimax(new_board, 2, False)
            if val > best_val:
                best_move = current_move
    else:
        best_val = +infinity
        for current_move in all_moves:
            new_board = board.copy_state()
            new_board.play_command(Command(current_move[0], current_move[1]))
            val = minimax(new_board, 4, alpha, beta, True)
            if val < best_val:
                best_move = current_move

    return best_move


def calscore(new_board):
    score = 0
    for entity in new_board.get_entities():
        team = entity.get_team()
        if team == Team.WHITE:
            score += 1
        else:
            score -= 1
    return score


def endgame(board):
    return board.get_winner() is not None


def minimax(board, depth, alpha, beta, maximizingPlayer):

    if depth == 0 or endgame(board):
        return calscore(board)

    if maximizingPlayer:
        max_eval = -infinity
        all_white_moves = board.get_legal_moves(Team.WHITE)
        for current_move in all_white_moves:
            new_board = board.copy_state()
            new_board.play_command(Command(current_move[0], current_move[1]))
            eval = minimax(new_board, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval

    else:
        min_eval = +infinity
        all_black_moves = board.get_legal_moves(Team.BLACK)
        for current_move in all_black_moves:
            new_board = board.copy_state()
            new_board.play_command(Command(current_move[0], current_move[1]))
            eval = minimax(new_board, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval


