import pygame
pygame.init()

# --- Colors ------------------------------------------------------------------

#                Red    Green   Blue
BLACK =         (0,     0,      0)
WHITE =         (255,   255,    255)
GREEN =         (0,     255,    0)
NAVY_BLUE =     (0,     0,      128)
MINT_CREAM =    (245,   255,    250)
DARK_BLUE =     (0,     0,      139)
PURPLE =        (128,   0,      128)
RED =           (255,   0,      0)
LIGHT_RED =     (155,   0,      0)


WALL_COLOR = MINT_CREAM
PATH_COLOR = DARK_BLUE

# --- Settings ----------------------------------------------------------------

GAME_NAME = 'Fight'
FPS = 60
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800


# --- Setup display -----------------------------------------------------------

game_display = pygame.display.set_mode((SCREEN_WIDTH+1, SCREEN_HEIGHT+1))

pygame.display.set_caption(GAME_NAME)
clock = pygame.time.Clock()



class Visualistation:

    def __init__(self, maze, players=[]):
        self.running = True
        self.maze = maze
        self.players = players

        self.cell_width = int(SCREEN_WIDTH / self.maze.width)
        self.cell_height = int(SCREEN_HEIGHT / self.maze.height)

    def quit(self):
        """Quit Game."""
        self.running = False
        pygame.quit()
        quit()

    def draw_cell(self, cell):
        if cell.walls[0]:  # North wall
            x1, y1 = cell.col * self.cell_width, cell.row * self.cell_height
            x2, y2 = (cell.col + 1) * self.cell_width, cell.row * self.cell_height
            pygame.draw.line(game_display, WALL_COLOR, (x1, y1), (x2, y2))

        if cell.walls[1]:  # East wall
            x1, y1 = (cell.col + 1) * self.cell_width, cell.row * self.cell_height
            x2, y2 = (cell.col + 1) * self.cell_width, (cell.row + 1) * self.cell_height
            pygame.draw.line(game_display, WALL_COLOR, (x1, y1), (x2, y2))

        if cell.walls[2]:  # South wall
            x1, y1 = cell.col * self.cell_width, (cell.row + 1) * self.cell_height
            x2, y2 = (cell.col + 1) * self.cell_width, (cell.row + 1) * self.cell_height
            pygame.draw.line(game_display, WALL_COLOR, (x1, y1), (x2, y2))

        if cell.walls[3]:  # West wall
            x1, y1 = cell.col * self.cell_width, cell.row * self.cell_height
            x2, y2 = cell.col * self.cell_width, (cell.row + 1) * self.cell_height
            pygame.draw.line(game_display, WALL_COLOR, (x1, y1), (x2, y2))

            
    def draw_cells(self):
        for row in self.maze.cells:
            for cell in row:
                self.draw_cell(cell)

    def draw_current_cell(self):
        rect = (self.maze.curr_cell.col * self.cell_width, 
                self.maze.curr_cell.row * self.cell_height,
                self.cell_width, self.cell_height)
        pygame.draw.rect(game_display, GREEN, rect)

    def draw_traveled(self):
        if self.players:
            for player in self.players:
                for (row, col) in player.ai.traveled:
                    rect = (col * self.cell_width, 
                            row * self.cell_height,
                            self.cell_width, self.cell_height)
                    pygame.draw.rect(game_display, LIGHT_RED, rect)

    def draw_player(self):
        if self.players:
            for player in self.players:
                rect = (player.col * self.cell_width, 
                    player.row * self.cell_height,
                    self.cell_width, self.cell_height)
                pygame.draw.rect(game_display, RED, rect)

    def update_display(self):
            
            # Draw background.
            game_display.fill(PATH_COLOR)
        
            # Draw assets.
            # self.draw_current_cell()
            # self.draw_traveled()
            self.draw_player()
            self.draw_cells()

            # Update
            pygame.display.update()
            clock.tick(FPS)

    def run(self):

        # Loop
        while self.running:

            # Controlls
            for event in pygame.event.get():
                # Quit
                if event.type == pygame.QUIT:
                    self.quit()


            self.update_display()
            


if __name__ == "__main__":
    vis = Visualistation(1)
    vis.run()



        