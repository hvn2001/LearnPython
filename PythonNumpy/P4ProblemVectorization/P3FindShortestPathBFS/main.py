# -----------------------------------------------------------------------------
# From Numpy to Python
# Copyright (2017) Nicolas P. Rougier - BSD license
# More information at https://github.com/rougier/numpy-book
# -----------------------------------------------------------------------------
import numpy as np
from collections import deque
import matplotlib.pyplot as plt
from scipy.ndimage import generic_filter


def build_maze(shape=(65, 65), complexity=0.75, density=0.50):
    """
    Build a maze using given complexity and density

    Parameters
    ==========

    shape : (rows,cols)
      Size of the maze

    complexity: float
      Mean length of islands (as a ratio of maze size)

    density: float
      Mean numbers of highland (as a ratio of maze surface)

    """

    # Only odd shapes
    shape = ((shape[0] // 2) * 2 + 1, (shape[1] // 2) * 2 + 1)

    # Adjust complexity and density relatively to maze size
    n_complexity = int(complexity * (shape[0] + shape[1]))
    n_density = int(density * (shape[0] * shape[1]))

    # Build actual maze
    Z = np.zeros(shape, dtype=bool)

    # Fill borders
    Z[0, :] = Z[-1, :] = Z[:, 0] = Z[:, -1] = 1

    # Islands starting point with a bias in favor of border
    P = np.random.normal(0, 0.5, (n_density, 2))
    P = 0.5 - np.maximum(-0.5, np.minimum(P, +0.5))
    P = (P * [shape[1], shape[0]]).astype(int)
    P = 2 * (P // 2)

    # Create islands
    for i in range(n_density):

        # Test for early stop: if all starting point are busy, this means we
        # won't be able to connect any island, so we stop.
        T = Z[2:-2:2, 2:-2:2]
        if T.sum() == T.size:
            break

        x, y = P[i]
        Z[y, x] = 1
        for j in range(n_complexity):
            neighbours = []
            if x > 1:
                neighbours.append([(y, x - 1), (y, x - 2)])
            if x < shape[1] - 2:
                neighbours.append([(y, x + 1), (y, x + 2)])
            if y > 1:
                neighbours.append([(y - 1, x), (y - 2, x)])
            if y < shape[0] - 2:
                neighbours.append([(y + 1, x), (y + 2, x)])
            if len(neighbours):
                choice = np.random.randint(len(neighbours))
                next_1, next_2 = neighbours[choice]
                if Z[next_2] == 0:
                    Z[next_1] = Z[next_2] = 1
                    y, x = next_2
            else:
                break
    return Z


# ------------------------------------------------------ find_shortest_path ---

def build_graph(maze):
    height, width = maze.shape
    graph = {(i, j): [] for j in range(width) for i in range(height) if not maze[i][j]}
    for row, col in graph.keys():
        if row < height - 1 and not maze[row + 1][col]:
            graph[(row, col)].append(("S", (row + 1, col)))
            graph[(row + 1, col)].append(("N", (row, col)))
        if col < width - 1 and not maze[row][col + 1]:
            graph[(row, col)].append(("E", (row, col + 1)))
            graph[(row, col + 1)].append(("W", (row, col)))
    return graph


def BreadthFirst(maze, start, goal):
    queue = deque([([start], start)])
    visited = set()
    graph = build_graph(maze)
    while queue:
        path, current = queue.popleft()
        if current == goal:
            return np.array(path)
        if current in visited:
            continue
        visited.add(current)
        for direction, neighbour in graph[current]:
            p = list(path)
            p.append(neighbour)
            queue.append((p, neighbour))
    return None


# -------------------------------------------------------------------- main ---
if __name__ == '__main__':
    Z = build_maze((41, 81))
    start, goal = (1, 1), (Z.shape[0] - 2, Z.shape[1] - 2)

    P = BreadthFirst(Z, start, goal)
    X, Y = P[:, 1], P[:, 0]

    # Visualization maze, gradient and shortest path
    plt.figure(figsize=(13, 13 * Z.shape[0] / Z.shape[1]))
    ax = plt.subplot(1, 1, 1, frameon=False)
    ax.imshow(Z, interpolation='nearest', cmap=plt.cm.gray_r, vmin=0.0, vmax=1.0)
    cmap = plt.cm.hot
    cmap.set_under(color='k', alpha=0.0)
    ax.scatter(X[1:-1], Y[1:-1], s=60,
               lw=1, marker='o', edgecolors='k', facecolors='w')
    ax.scatter(X[[0, -1]], Y[[0, -1]], s=60,
               lw=3, marker='x', color=['w', 'k'])
    ax.set_xticks([])
    ax.set_yticks([])

    plt.tight_layout()
    plt.savefig("output/maze.png")
    plt.show()
