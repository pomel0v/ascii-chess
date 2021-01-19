from chess.colors import Color
from chess.knight import Knight
from chess.rook import Rook
from chess.board import Board
import pytest


def test_initial_board_size():
    """ поле правильного размера 8х8 """
    board = Board()


def test_white_first():
    pass


def test_initial_setup():
    """ начальный спавн фигур """ 
    board = Board()
    
    fig = board.field[0][0]
    assert fig.color == Color.WHITE
    assert isinstance(fig, Rook)


def test_cant_move_wrong_command():
    board = Board()
    assert not board.can_move(10, 10, 0, 0)


def test_cant_move_same_place():
    board = Board()
    assert not board.can_move(0, 0, 0, 0)


def test_cant_move_no_figure():
    board = Board()
    assert not board.can_move(5, 5, 5, 5)