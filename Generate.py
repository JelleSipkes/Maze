import threading
import pickle

from classes.Maze import Maze

VISUALISE   = False
SAVE        = True

if __name__ == "__main__":
    maze = Maze(100, 100)

    if VISUALISE:
        from classes.Visualisation import Visualistation
        vis = Visualistation(maze)
        run_visualisation = threading.Thread(target=vis.run)
        run_visualisation.start()

    generate = threading.Thread(target=maze.generate)
    generate.start()

    if SAVE:
        generate.join()
        file_name = "maze.pkl"
        with open(file_name, "wb") as file:
            pickle.dump(maze, file)
            print("maze saved to", file_name)
