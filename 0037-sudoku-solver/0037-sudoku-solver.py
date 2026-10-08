class Solution:

  def solveSudoku(self, board: list[list[str]]) -> None:
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    empty = []

    for r in range(9):
      for c in range(9):
        val = board[r][c]
        if val != ".":
          rows[r].add(val)
          cols[c].add(val)
          boxes[(r // 3) * 3 + (c // 3)].add(val)
        else:
          empty.append((r, c))

    def backtrack(idx: int) -> bool:
      if idx == len(empty):
        return True

      r, c = empty[idx]
      box_idx = (r // 3) * 3 + (c // 3)

      for digit in map(str, range(1, 10)):
        if (
            digit not in rows[r]
            and digit not in cols[c]
            and digit not in boxes[box_idx]
        ):
          board[r][c] = digit
          rows[r].add(digit)
          cols[c].add(digit)
          boxes[box_idx].add(digit)

          if backtrack(idx + 1):
            return True

          board[r][c] = "."
          rows[r].remove(digit)
          cols[c].remove(digit)
          boxes[box_idx].remove(digit)

      return False

    backtrack(0)
        