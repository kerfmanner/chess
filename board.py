'''Chess board module'''
from pieces import Pawn, Rook, Knight, Bishop, Queen, King

class ChessBoard:

    def __init__(self, size):
        self._size = size
        self.grid = [[Square(color=((i+j) % 2)) for i in range(size)] for j in range(size)]
        self.white_king_coordinates = None
        self.black_king_coordinates = None

    def setup_default_position(self):

        if self._size != 8:
            raise ValueError('The size of default chess board should be 8')

        for i in range(self._size):
            self.grid[1][i].piece = Pawn(1)
            self.grid[6][i].piece = Pawn(0)

        for i in (0, 7):
            self.grid[0][i].piece = Rook(1)
            self.grid[7][i].piece = Rook(0)

        for i in (1,6):
            self.grid[0][i].piece = Knight(1)
            self.grid[7][i].piece = Knight(0)

        for i in (2,5):
            self.grid[0][i].piece = Bishop(1)
            self.grid[7][i].piece = Bishop(0)

        self.grid[0][3].piece = Queen(1)
        self.grid[7][3].piece = Queen(0)

        self.grid[0][4].piece = King(1)
        self.grid[7][4].piece = King(0)

        self.white_king_coordinates = (0, 4)
        self.black_king_coordinates = (7, 4)

    def __str__(self):
        message = 'Black view(0 - Black, 1 - White):\n'
        message += '  '.join([' ','A','B','C','D','E','F','G','H']) + '\n'
        for index, row in enumerate(self.grid):
            message += f'{8 - index} ' + ' '.join(str(cell) for cell in row) + f' {8 - index}'
            message += '\n'
        message += '  '.join([' ','A','B','C','D','E','F','G','H'])
        return message

    def __repr__(self):
        return f'(Size = {self._size}, grid = {self.grid})'

class Square:
    def __init__(self, color:int|None=None):
        self._color = color
        self._piece = None

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):
        self._color = color

    @property
    def piece(self):
        return self._piece
    
    @piece.setter
    def piece(self, piece):
        self._piece = piece

    def __str__(self):
        if self.piece is None:
            return '--'
        return f'{self.piece}'

    def __repr__(self):
        return f'(Color = {self.color}, piece = {self.piece}'
