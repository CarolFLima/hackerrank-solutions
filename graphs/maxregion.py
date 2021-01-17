
def countFilledCells(grid, i, j):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]): 
        return 0
    if grid[i][j] == 0: 
        return 0
    count = 1
    grid[i][j] = 0
    count += countFilledCells(grid, i + 1, j)
    count += countFilledCells(grid, i - 1, j)
    count += countFilledCells(grid, i, j + 1)
    count += countFilledCells(grid, i, j - 1)
    count += countFilledCells(grid, i + 1, j + 1)
    count += countFilledCells(grid, i - 1, j - 1)
    count += countFilledCells(grid, i - 1, j + 1)
    count += countFilledCells(grid, i + 1, j - 1)
    return count


def maxRegion(grid):
    n = len(grid)
    m = len(grid[0])
    max_region = 0

    for i in range(n):
        for j in range(m):
            max_region = max(max_region, countFilledCells(grid, i, j))

    return max_region

grid = [[1, 1, 0, 0],
[0, 1, 1, 0],
[0, 0, 1, 0],
[1, 0, 0, 0]]

print(maxRegion(grid))