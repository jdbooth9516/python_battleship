class Ship:
    def __init__(self):
        self.name = "destroyer"
        self.size = 3
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