from collections import defaultdict


class Solution:

  def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    groups = defaultdict(list)

    for s in strs:
      # Character count tuple as dictionary key
      count = [0] * 26
      for char in s:
        count[ord(char) - ord("a")] += 1
      groups[tuple(count)].append(s)

    return list(groups.values())
        