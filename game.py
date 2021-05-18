from board import Board
from pieces import Ship


class Game:
    def __init__(self):
        self.board = Board()
        self.piece = Ship()

    def run_game(self):
        self.show_board()
        self.place_piece()

    def place_piece(self):
        dirct = self.piece.set_direction()
        col = self.piece.set_piece_colum()
        row = self.piece.set_piece_row()
        self.board.target[row][col] = ' D '
        if dirct == 'vertical':
            for i in range(self.piece.size ):
                self.board.target[row + i][col] = ' D '
        self.show_board()

    def show_board(self):
        player_1_board = self.board.target
        length = len(player_1_board)
        for i in range(length):
            print(player_1_board[i])
