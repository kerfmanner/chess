from abc import ABC, abstractmethod

class Piece(ABC):

    def __init__(self):
        self.colour : None|int = None
        self.has_moved :bool = False

    def set_colour(self, colour:int):
        if isinstance(colour, int):
            self.colour = colour
        raise ValueError('Color is presented by integer.')

    @abstractmethod
    def check_move(self, board, piece):
        ...

    @abstractmethod
    def __repr__(self):
        ...

class Pawn(Piece):

    def check_move(self, board, piece):
        ...
    
    def __repr__(self):
        return 'P'

class Knight(Piece):

    def check_move(self, board, piece):
        ...
    
    def __repr__(self):
        return 'N'

class Bishop(Piece):

    def check_move(self, board, piece):
        ...
    
    def __repr__(self):
        return 'B'

class Rook(Piece):

    def check_move(self, board, piece):
        ...
    
    def __repr__(self):
        return 'R'

class Queen(Piece):

    def check_move(self, board, piece):
        ...
    
    def __repr__(self):
        return 'Q'

class King(Piece):

    def check_move(self, board, piece):
        ...

    def __repr__(self):
        return 'K'