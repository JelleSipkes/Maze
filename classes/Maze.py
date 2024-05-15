import random
import time

from classes.Cell import Cell

class Maze:

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.cells = [[Cell(row, col) for col in range(self.width)]
                                      for row in range(self.height)]
        self.curr_cell = self.cells[0][0]
        
    def generate(self) -> None:
        stack = [self.curr_cell]
        
        while True:
            # time.sleep(0.00001)
            self.curr_cell.visited = True
            unvisited_neigbors = self._get_unvisited_neigbors(self.curr_cell)
            
            if unvisited_neigbors:
                stack.append(self.curr_cell)
                next_cell = random.choice(unvisited_neigbors)
                self._remove_wall(self.curr_cell, next_cell)
                self.curr_cell = next_cell
            else:
                if not stack:
                    break
                self.curr_cell = stack.pop()


    def _get_unvisited_neigbors(self, cell : Cell) -> list:

        # List all neigbors.
        neigbors = []
        if cell.row != 0: 
            neigbors.append(self.cells[cell.row-1][cell.col])
        if cell.col != 0: 
            neigbors.append(self.cells[cell.row][cell.col-1])
        if cell.row != self.height-1: 
            neigbors.append(self.cells[cell.row+1][cell.col])
        if cell.col != self.width-1: 
            neigbors.append(self.cells[cell.row][cell.col+1])

        # List unvisited neigbors.
        unvisited_neigbors = []
        for neigbor in neigbors:
            if not neigbor.visited:
                unvisited_neigbors.append(neigbor)
        
        return unvisited_neigbors
 
    def _remove_wall(self, cell0: Cell, cell1: Cell) -> None:
        if cell0.row == cell1.row-1:
            cell0.walls[2] = False
            cell1.walls[0] = False
        if cell0.row == cell1.row+1:
            cell0.walls[0] = False
            cell1.walls[2] = False
        if cell0.col == cell1.col-1:
            cell0.walls[1] = False
            cell1.walls[3] = False
        if cell0.col == cell1.col+1:
            cell0.walls[3] = False
            cell1.walls[1] = False


if __name__ == "__main__":
    maze = Maze(50, 50)