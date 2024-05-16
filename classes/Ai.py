class Ai_0:

    def __init__(self) -> None:
        self.traveled = []
        self.stack = []


    def get_direction(self, row: int, col: int, walls: list):
        self.traveled.append((row,col))

        # If new way to explore.
        for i, wall in enumerate(walls):
            if not wall:
                if (i == 0 and (row-1, col) not in self.traveled) or \
                   (i == 1 and (row, col+1) not in self.traveled) or \
                   (i == 2 and (row+1, col) not in self.traveled) or \
                   (i == 3 and (row, col-1) not in self.traveled):
                    
                    self.stack.append((row, col))
                    return i
                
        
        # If no new way to explore.
        (row2, col2) = self.stack.pop()
        if row == row2 + 1 : return 0
        elif col == col2 - 1 : return 1
        elif row == row2 - 1 : return 2
        elif col == col2 + 1 : return 3

class Ai_1:
    """ Start with checking east, then rotate clockwise. """

    def __init__(self) -> None:
        self.traveled = []
        self.stack = []


    def get_direction(self, row: int, col: int, walls: list):
        self.traveled.append((row,col))

        # If new way to explore.
        for i in range(4):
            i = (i + 1) % 4
            wall = walls[i]
            if not wall:
                if (i == 0 and (row-1, col) not in self.traveled) or \
                   (i == 1 and (row, col+1) not in self.traveled) or \
                   (i == 2 and (row+1, col) not in self.traveled) or \
                   (i == 3 and (row, col-1) not in self.traveled):
                    
                    self.stack.append((row, col))
                    return i
                
        
        # If no new way to explore.
        (row2, col2) = self.stack.pop()
        if row == row2 + 1 : return 0
        elif col == col2 - 1 : return 1
        elif row == row2 - 1 : return 2
        elif col == col2 + 1 : return 3
        
class Ai_2:
    """ Start with checking east, then rotate clockwise. """

    def __init__(self) -> None:
        self.traveled = []
        self.stack = []

    def get_direction(self, row: int, col: int, walls: list):
        self.traveled.append((row,col))

        # If new way to explore.
        if row > col:
            directions = [1, 2, 0, 3]
        else:
            directions = [2, 1, 3, 0]

        for i in directions:
            wall = walls[i]
            if not wall:
                if (i == 0 and (row-1, col) not in self.traveled) or \
                   (i == 1 and (row, col+1) not in self.traveled) or \
                   (i == 2 and (row+1, col) not in self.traveled) or \
                   (i == 3 and (row, col-1) not in self.traveled):
                    
                    self.stack.append((row, col))
                    return i
                
        
        # If no new way to explore.
        (row2, col2) = self.stack.pop()
        if row == row2 + 1 : return 0
        elif col == col2 - 1 : return 1
        elif row == row2 - 1 : return 2
        elif col == col2 + 1 : return 3