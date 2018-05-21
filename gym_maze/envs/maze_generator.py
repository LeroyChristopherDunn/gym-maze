import os
from gym_maze.envs.maze_view_2d import Maze

num_mazes = 50
maze_size = 100


def get_registration_boilerplate(maze_file_name):
    return """
register(
\tid='""" + maze_file_name.replace("_", "-") + """',
\tentry_point='gym_maze.envs:MazeEnv',
\tkwargs={'maze_file': '""" + maze_file_name + """.npy'},
\tmax_episode_steps=1000000,
)"""


if __name__ == "__main__":

    dir_name = os.path.join(os.getcwd(), "maze_samples")
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)

    maze_ids = []
    size_string = str(maze_size) + "x" + str(maze_size)

    # increment number until it finds a name that is not being used already (max maze_999)
    maze_path = None
    for i in range(1, num_mazes+1):
        maze_prefix = "maze_custom_" + size_string + "_v%03d" % i
        maze_ids.append(maze_prefix)
        maze_file_name = maze_prefix + ".npy"
        maze_path = os.path.join(dir_name, maze_file_name)
        if not os.path.exists(maze_path):
            maze = Maze(maze_size=(maze_size, maze_size))
            maze.save_maze(maze_path)
            print("New maze generated and saved at %s." % maze_path)

    print("")
    print("Registration boilerplate: ")
    print("")
    print("# region custom " + size_string)
    for maze_file_name in maze_ids:
        print(get_registration_boilerplate(maze_file_name))
    print("# endregion")

