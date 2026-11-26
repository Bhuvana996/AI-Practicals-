import numpy as np

grid = np.zeros((3, 3))
gamma = 0.9

for i in range(10):
    new = grid.copy()
    for r in range(3):
        for c in range(3):
            if (r, c) == (2, 2):
                continue
            new[r, c] = -1 + gamma * max(
                grid[max(0,r-1),c],
                grid[min(2,r+1),c],
                grid[r,max(0,c-1)],
                grid[r,min(2,c+1)]
            )
    grid = new

print(grid)
