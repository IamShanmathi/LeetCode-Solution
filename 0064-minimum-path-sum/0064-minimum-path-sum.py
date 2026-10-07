class Solution:

  def minPathSum(self, grid: list[list[int]]) -> int:
    ROWS, COLS = len(grid), len(grid[0])

    # Fill the first row (can only move right)
    for c in range(1, COLS):
      grid[0][c] += grid[0][c - 1]

    # Fill the first column (can only move down)
    for r in range(1, ROWS):
      grid[r][0] += grid[r - 1][0]

    # Fill the rest of the grid
    for r in range(1, ROWS):
      for c in range(1, COLS):
        grid[r][c] += min(grid[r - 1][c], grid[r][c - 1])

    return grid[-1][-1]