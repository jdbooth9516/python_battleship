from board import Board
from pieces import Ship
from players import Player


class Game:
    def __init__(self):
        self.player_1 = Player()
        self.player_2 = Player()
        self.turn = 1
        self.run = False

    def run_game(self):
        # ADD INSTRUCTIONS ABOVE HERE
        self.run = True
        print("Player 1")
        self.player_1.set_name()
        print("Player 2 ")
        self.player_2.set_name()
        # PLAYER 1 PLACES PIECES
        self.show_board()
        self.place_piece()
        self.clear_screen()
        #PLAYER 2 PLACE PIECES
        self.show_board()
        self.place_piece()
        self.clear_screen()
        #START MAIN LOOP HERE
        self.main()

    def main(self):
        while self.run == True:
            self.show_board()
            self.attack()


    def place_piece(self):
        if self.turn == 1:
            length = len(self.player_1.pieces)
            print(f'{self.player_1.name} please place your pieces')
            for i in range(length):

                dirct = self.player_1.pieces[i].set_direction()
                col = self.player_1.pieces[i].set_piece_colum()
                row = self.player_1.pieces[i].set_piece_row()
                self.player_1.own_board.grid[row][col] = self.player_1.pieces[i].id

                if dirct == 'vertical':
                    for j in range(self.player_1.pieces[i].size):
                        print(self.player_1.pieces[i].size)
                        self.player_1.own_board.grid[row + j][col] = self.player_1.pieces[i].id
                        self.show_board()

                elif dirct == 'horizontal':
                    for j in range(self.player_1.pieces[i].size):
                        self.player_1.own_board.grid[row][col + j] = self.player_1.pieces[i].id
                        self.show_board()

        else:
            length = len(self.player_2.pieces)
            print(f'{self.player_2.name} please place your pieces')
            for i in range(length):

                dirct = self.player_2.pieces[i].set_direction()
                col = self.player_2.pieces[i].set_piece_colum()
                row = self.player_2.pieces[i].set_piece_row()
                self.player_2.own_board.grid[row][col] = self.player_2.pieces[i].id

                if dirct == 'vertical':
                    for j in range(self.player_2.pieces[i].size):
                        print(self.player_2.pieces[i].size)
                        self.player_2.own_board.grid[row + j][col] = self.player_2.pieces[i].id
                        self.show_board()

                elif dirct == 'horizontal':
                    for j in range(self.player_2.pieces[i].size):
                        self.player_2.own_board.grid[row][col + j] = self.player_2.pieces[i].id
                        self.show_board()

        self.handle_turn()

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

    def handle_turn(self):
        if self.turn == 1:
            self.turn = 2
        else:
            self.turn = 1

    def attack(self):
        col = int(input('Choose a column to attack: '))
        row = int(input('Choose a row to attack: '))

        if self.turn == 1:
            if self.player_2.own_board.grid[row][col] == ' # ':
                print("MISSED")
                self.player_1.attack_board.grid[row][col] = ' M '
            elif self.player_2.own_board.grid[row][col] == ' D ':
                print("HIT")
                self.player_1.attack_board.grid[row][col] = ' H '
                self.player_2.own_board.grid[row][col] = ' H '
            self.handle_turn()
            self.clear_screen()

        elif self.turn == 2:
            if self.player_1.own_board.grid[row][col] == ' # ':
                print("MISSED")
                self.player_2.attack_board.grid[row][col] = ' M '
            elif self.player_1.own_board.grid[row][col] == ' D ':
                print("HIT")
                self.player_2.attack_board.grid[row][col] = ' H '
                self.player_1.own_board.grid[row][col] = ' H '
            self.handle_turn()
            self.clear_screen()
            self.run = False


    def clear_screen(self):
        for i in range(20):
            print()
