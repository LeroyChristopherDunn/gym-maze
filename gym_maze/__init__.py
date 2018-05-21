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

# region custom 10x10

register(
    id='maze-custom-10x10-v001',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_10x10_v001.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-10x10-v002',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_10x10_v002.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-10x10-v003',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_10x10_v003.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-10x10-v004',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_10x10_v004.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-10x10-v005',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_10x10_v005.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-10x10-v006',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_10x10_v006.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-10x10-v007',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_10x10_v007.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-10x10-v008',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_10x10_v008.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-10x10-v009',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_10x10_v009.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-10x10-v010',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_10x10_v010.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-10x10-v011',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_10x10_v011.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-10x10-v012',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_10x10_v012.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-10x10-v013',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_10x10_v013.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-10x10-v014',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_10x10_v014.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-10x10-v015',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_10x10_v015.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-10x10-v016',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_10x10_v016.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-10x10-v017',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_10x10_v017.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-10x10-v018',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_10x10_v018.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-10x10-v019',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_10x10_v019.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-10x10-v020',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_10x10_v020.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-10x10-v021',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_10x10_v021.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-10x10-v022',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_10x10_v022.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-10x10-v023',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_10x10_v023.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-10x10-v024',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_10x10_v024.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-10x10-v025',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_10x10_v025.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-10x10-v026',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_10x10_v026.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-10x10-v027',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_10x10_v027.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-10x10-v028',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_10x10_v028.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-10x10-v029',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_10x10_v029.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-10x10-v030',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_10x10_v030.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-10x10-v031',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_10x10_v031.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-10x10-v032',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_10x10_v032.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-10x10-v033',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_10x10_v033.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-10x10-v034',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_10x10_v034.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-10x10-v035',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_10x10_v035.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-10x10-v036',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_10x10_v036.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-10x10-v037',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_10x10_v037.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-10x10-v038',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_10x10_v038.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-10x10-v039',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_10x10_v039.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-10x10-v040',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_10x10_v040.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-10x10-v041',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_10x10_v041.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-10x10-v042',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_10x10_v042.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-10x10-v043',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_10x10_v043.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-10x10-v044',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_10x10_v044.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-10x10-v045',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_10x10_v045.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-10x10-v046',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_10x10_v046.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-10x10-v047',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_10x10_v047.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-10x10-v048',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_10x10_v048.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-10x10-v049',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_10x10_v049.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-10x10-v050',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_10x10_v050.npy'},
    max_episode_steps=1000000,
)
# endregion

# region custom 100x100

register(
    id='maze-custom-100x100-v001',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_100x100_v001.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-100x100-v002',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_100x100_v002.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-100x100-v003',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_100x100_v003.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-100x100-v004',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_100x100_v004.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-100x100-v005',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_100x100_v005.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-100x100-v006',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_100x100_v006.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-100x100-v007',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_100x100_v007.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-100x100-v008',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_100x100_v008.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-100x100-v009',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_100x100_v009.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-100x100-v010',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_100x100_v010.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-100x100-v011',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_100x100_v011.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-100x100-v012',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_100x100_v012.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-100x100-v013',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_100x100_v013.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-100x100-v014',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_100x100_v014.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-100x100-v015',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_100x100_v015.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-100x100-v016',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_100x100_v016.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-100x100-v017',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_100x100_v017.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-100x100-v018',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_100x100_v018.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-100x100-v019',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_100x100_v019.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-100x100-v020',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_100x100_v020.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-100x100-v021',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_100x100_v021.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-100x100-v022',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_100x100_v022.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-100x100-v023',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_100x100_v023.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-100x100-v024',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_100x100_v024.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-100x100-v025',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_100x100_v025.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-100x100-v026',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_100x100_v026.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-100x100-v027',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_100x100_v027.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-100x100-v028',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_100x100_v028.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-100x100-v029',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_100x100_v029.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-100x100-v030',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_100x100_v030.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-100x100-v031',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_100x100_v031.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-100x100-v032',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_100x100_v032.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-100x100-v033',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_100x100_v033.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-100x100-v034',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_100x100_v034.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-100x100-v035',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_100x100_v035.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-100x100-v036',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_100x100_v036.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-100x100-v037',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_100x100_v037.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-100x100-v038',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_100x100_v038.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-100x100-v039',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_100x100_v039.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-100x100-v040',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_100x100_v040.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-100x100-v041',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_100x100_v041.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-100x100-v042',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_100x100_v042.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-100x100-v043',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_100x100_v043.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-100x100-v044',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_100x100_v044.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-100x100-v045',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_100x100_v045.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-100x100-v046',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_100x100_v046.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-100x100-v047',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_100x100_v047.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-100x100-v048',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_100x100_v048.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-100x100-v049',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_100x100_v049.npy'},
    max_episode_steps=1000000,
)

register(
    id='maze-custom-100x100-v050',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={'maze_file': 'maze_custom_100x100_v050.npy'},
    max_episode_steps=1000000,
)
# endregion


