from window import Window
from maze import Maze


def main():
    maze_window = Window(1000, 800)
    maze = Maze(10, 10, 11, 14, 70, 70, maze_window,11)
    maze._break_entrance_and_exit() 
    maze._break_walls_r(0,0)
    maze._reset_cells_visited()
    maze.solve()


    maze_window.wait_for_close()




main()
