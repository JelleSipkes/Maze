import threading
import time

from classes.Maze           import Maze

VISUALISE = True

if __name__ == "__main__":
    maze = Maze(90, 90)

    if VISUALISE:
        from classes.Visualisation import Visualistation
        vis = Visualistation(maze)
        run_visualisation = threading.Thread(target=vis.run)
        run_visualisation.start()

    generate = threading.Thread(target=maze.generate)
    generate.start()
    