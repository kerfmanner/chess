from abc import ABC, abstractmethod


class Piece(ABC):
    '''
    0 - Black
    1 - White
    '''
    def __init__(self, color: None|int = None):
        self._color: None | int = color
        self.has_moved: bool = False

    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, color):
        if isinstance(color, int):
            self.color = color
        raise ValueError('Color should be presented by integer')

    @abstractmethod
    def check_move(self, board, move, enemy_move, checked: bool) -> bool: ...

    @abstractmethod
    def __repr__(self): ...


class Pawn(Piece):

    def check_move(self, board, move, enemy_move, checked: bool) -> bool: ...

    def __repr__(self):
        return f"{self.color}P"


class Knight(Piece):

    def check_move(self, board, move, enemy_move, checked: bool) -> bool: ...

    def __repr__(self):
        return f"{self.color}N"


class Bishop(Piece):

    def check_move(self, board, move, enemy_move, checked: bool) -> bool: ...

    def __repr__(self):
        return f"{self.color}B"


class Rook(Piece):

    def check_move(self, board, move, enemy_move, checked: bool) -> bool: ...

    def __repr__(self):
        return f"{self.color}R"


class Queen(Piece):

    def check_move(self, board, move, enemy_move, checked: bool) -> bool: ...

    def __repr__(self):
        return f"{self.color}Q"


class King(Piece):

    def check_move(self, board, move, enemy_move, checked: bool) -> bool: ...

    def __repr__(self):
        return f"{self.color}K"
