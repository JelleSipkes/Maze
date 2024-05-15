class Cell:

    def __init__(self, row: int, col: int) -> None:
        self.row = row
        self.col = col
        self.walls = [True for _ in range(4)]

        self.visited = False