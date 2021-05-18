class Player:
    def __init__(self):
        self.name = ""
        self.attack_board = Board()
        self.own_board = Board()
        self.pieces = []

    def set_name(self):
        name = input("Please enter a name: ")
        self.name = name