from board import Board
from pieces import Ship
from players import Player


class Game:
    def __init__(self):
        self.piece = Ship()
        self.player_1 = Player()
        self.player_2 = Player()
        self.turn = 1

    def run_game(self):
        print("Player 1")
        self.player_1.set_name()
        print("Player 2 ")
        self.player_2.set_name()
        self.show_board()
        self.place_piece()

    def place_piece(self):
        dirct = self.piece.set_direction()
        col = self.piece.set_piece_colum()
        row = self.piece.set_piece_row()
        self.player_1.own_board.grid[row][col] = ' D '
        if dirct == 'vertical':
            for i in range(self.piece.size):
                self.player_1.own_board.grid[row + i][col] = ' D '
        self.show_board()

    def show_board(self):
        if self.turn == 1:
            player_1_attack = self.player_1.attack_board.grid
            player_1_own = self.player_1.own_board.grid
            length = len(player_1_attack)
            print("ATTACK BOARD")
            for i in range(length):
                print(player_1_attack[i])
            print("OWN_BOARD")
            for i in range(length):
                print(player_1_own[i])
        elif self.turn == 2:
            player_2_attack = self.player_2.attack_board.grid
            player_2_own = self.player_2.own_board.grid
            length = len(player_2_attack)
            print("ATTACK BOARD")
            for i in range(length):
                print(player_2_attack[i])
            print("OWN_BOARD")
            for i in range(length):
                print(player_2_own[i])

