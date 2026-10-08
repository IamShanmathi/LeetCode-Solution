class Solution:

  def combinationSum(
      self, candidates: list[int], target: int
  ) -> list[list[int]]:
    res = []

    def backtrack(start: int, path: list[int], current_sum: int):
      if current_sum == target:
        res.append(list(path))
        return
      if current_sum > target:
        return

      for i in range(start, len(candidates)):
        path.append(candidates[i])
        backtrack(i, path, current_sum + candidates[i])
        path.pop()

    backtrack(0, [], 0)
    return res
        