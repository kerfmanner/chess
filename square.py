class Square:
    def __init__(self, position: tuple, color: int | None = None):
        self._color = color
        self._piece = None
        self.position = position

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
            return "--"
        return f"{self.piece}"

    def __repr__(self):
        return f"(Color = {self.color}, piece = {self.piece}"
