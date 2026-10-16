class Solution:
    def __init__(self):
        self.memo = {}

    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):
            return False
        
        key = (s1, s2)
        if key in self.memo:
            return self.memo[key]
        
        n = len(s1)
        for i in range(1, n):
            # Check non-swapped
            if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])):
                self.memo[key] = True
                return True
            # Check swapped
            if (self.isScramble(s1[:i], s2[n-i:]) and self.isScramble(s1[i:], s2[:n-i])):
                self.memo[key] = True
                return True
                
        self.memo[key] = False
        return False
        