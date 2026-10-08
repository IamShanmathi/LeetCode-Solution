class Solution:

  def combinationSum2(
      self, candidates: list[int], target: int
  ) -> list[list[int]]:
    candidates.sort()
    res = []

    def backtrack(start: int, path: list[int], remain: int):
      if remain == 0:
        res.append(list(path))
        return

      for i in range(start, len(candidates)):
        # Skip duplicates at the same tree depth
        if i > start and candidates[i] == candidates[i - 1]:
          continue
        if candidates[i] > remain:
          break

        path.append(candidates[i])
        backtrack(i + 1, path, remain - candidates[i])
        path.pop()

    backtrack(0, [], target)
    return res
        