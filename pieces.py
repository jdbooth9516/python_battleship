class Ship:
    def __init__(self):
        self.name = ''
        self.size = 0
        self.direction = ' '

    def set_direction(self):
        direction = input("pick a direction to place the ship: type 'h' for horizontal or 'v' for vertical: ")
        if direction == 'h':
            self.direction = 'horizontal'
            return self.direction
        else:
            self.direction = 'vertical'
            return self.direction

    def set_piece_colum(self):
        column_cord = int(input('select column cordinate to place your piece: '))
        return column_cord

    def set_piece_row(self):
        row_cord = int(input('select row cordinate to place your piece: '))
        return row_cord

class Destroyer(Ship):
    def __init__(self):
        super().__init__()
        self.name = 'Destroyer'
        self.size = 2

class Submarine(Ship):
    def __init__(self):
        super().__init__()
        self.name = 'Submarine'
        self.size = 3

class Battleship(Ship):
    def __init__(self):
        super().__init__()
        self.name = 'Battleship'
        self.size = 3

class Aircraft_carrier(Ship):
    def __init__(self):
        super().__init__()
        self.name = 'Aircraft_carrier'
        self.size = 5
        