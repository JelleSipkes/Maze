import threading
import pickle
import time

from classes.Player import Player
from classes.Ai     import *

FILE_NAME = "maze.pkl"
VISUALISE = False

# Read maze file.
with open(FILE_NAME, "rb") as file:
    maze = pickle.load(file)
print("Maze loaded from file")

# Player.
ai_0 = Ai_0()
ai_1 = Ai_1()
ai_2 = Ai_2()
players = [Player(maze, ai_0), Player(maze, ai_1), Player(maze, ai_2)]
# players = [Player(maze, ai_2)]


if VISUALISE:
    from classes.Visualisation import Visualistation
    vis = Visualistation(maze, players)
    run_visualisation = threading.Thread(target=vis.run)
    run_visualisation.start()

for player in players:
    run_player = threading.Thread(target=player.play)
    run_player.start()

 