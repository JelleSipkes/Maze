import time

class Player:

    def __init__(self, maze, ai) -> None:
        self.maze = maze
        self.ai = ai
        self.row = 0
        self.col = 0

    def move(self, direction: int) -> None:
        curr_cell = self.maze.cells[self.row][self.col]
        if not curr_cell.walls[direction]:
            if direction == 0: self.row -= 1
            elif direction == 1: self.col += 1
            elif direction == 2: self.row += 1
            elif direction == 3: self.col -= 1

    def play(self):
        t = 0
        while not (self.row == self.maze.height-1 \
              and self.col == self.maze.width-1):
            # time.sleep(0.001)
            direction = self.ai.get_direction(self.row, self.col, self.maze.cells[self.row][self.col].walls)
            self.move(direction)
            t += 1
        print(str(self.ai)[12:16], "Done! it took", t, "steps")
