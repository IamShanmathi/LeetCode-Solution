class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        result, cur, num_of_letters = [], [], 0
        
        for w in words:
            if num_of_letters + len(w) + len(cur) > maxWidth:
                for i in range(maxWidth - num_of_letters):
                    cur[i % (len(cur) - 1 or 1)] += ' '
                result.append(''.join(cur))
                cur, num_of_letters = [], 0
            cur.append(w)
            num_of_letters += len(w)
            
        return result + [' '.join(cur).ljust(maxWidth)]
        