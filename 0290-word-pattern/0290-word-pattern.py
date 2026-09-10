class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False

        mapping = {}
        used = set()

        for i in range(len(pattern)):
            ch = pattern[i]
            word = words[i]

            if ch in mapping:
                if mapping[ch] != word:
                    return False
            else:
                if word in used:
                    return False

                mapping[ch] = word
                used.add(word)

        return True
        