class Solution:

  def isMatch(self, s: str, p: str) -> bool:
    s_ptr = p_ptr = 0
    star_idx = s_match_idx = -1

    while s_ptr < len(s):
      # Case 1: Exact match or '?' match
      if p_ptr < len(p) and (p[p_ptr] == s[s_ptr] or p[p_ptr] == "?"):
        s_ptr += 1
        p_ptr += 1
      # Case 2: '*' match found
      elif p_ptr < len(p) and p[p_ptr] == "*":
        star_idx = p_ptr
        s_match_idx = s_ptr
        p_ptr += 1
      # Case 3: Backtrack to last '*' found
      elif star_idx != -1:
        p_ptr = star_idx + 1
        s_match_idx += 1
        s_ptr = s_match_idx
      else:
        return False

    # Check for remaining trailing '*' in pattern
    while p_ptr < len(p) and p[p_ptr] == "*":
      p_ptr += 1

    return p_ptr == len(p)
        