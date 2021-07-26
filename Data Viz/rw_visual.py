import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making random walks, as long as the program is active.
while True:
    # Make a random walk.
    rw = RandomWalk()
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('dark_background')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)

    # Emphasize the first and the last points.
    ax.scatter(0, 0, c='green', edgecolors='none', s=25)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=25)

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # plt.savefig("random_walk_5.png", bbox_inches='tight')
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
