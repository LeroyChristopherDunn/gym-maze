from gym.envs.registration import register

register(
    id='maze-v0',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze2d_5x5.npy'},
    max_episode_steps=2000,
)

register(
    id='maze-sample-5x5-v0',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze2d_5x5.npy'},
    max_episode_steps=2000,
)

register(
    id='maze-random-5x5-v0',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_size': (5, 5)},
    max_episode_steps=2000,
    nondeterministic=True,
)

register(
    id='maze-sample-10x10-v0',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze2d_10x10.npy'},
    max_episode_steps=10000,
)

register(
    id='maze-random-10x10-v0',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_size': (10, 10)},
    max_episode_steps=10000,
    nondeterministic=True,
)

register(
    id='maze-sample-3x3-v0',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze2d_3x3.npy'},
    max_episode_steps=1000,
)

register(
    id='maze-random-3x3-v0',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_size': (3, 3)},
    max_episode_steps=1000,
    nondeterministic=True,
)

register(
    id='maze-sample-100x100-v0',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze2d_100x100.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-random-100x100-v0',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_size': (100, 100)},
    max_episode_steps=1000000,
    nondeterministic=True,
)

register(
    id='maze-random-10x10-plus-v0',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_size': (10, 10), 'mode': 'plus'},
    max_episode_steps=1000000,
    nondeterministic=True,
)

register(
    id='maze-random-20x20-plus-v0',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_size': (20, 20), 'mode': 'plus'},
    max_episode_steps=1000000,
    nondeterministic=True,
)

register(
    id='maze-random-30x30-plus-v0',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_size': (30, 30), 'mode': 'plus'},
    max_episode_steps=1000000,
    nondeterministic=True,
)
