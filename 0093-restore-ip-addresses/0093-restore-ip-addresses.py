class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        res = []
        if len(s) > 12:
            return res
            
        def backtrack(start, path):
            if len(path) == 4:
                if start == len(s):
                    res.append(".".join(path))
                return
                
            for i in range(start, min(start + 3, len(s))):
                segment = s[start:i+1]
                # Check valid segment: no leading zeros unless single '0', <= 255
                if (segment == "0" or (segment[0] != "0" and int(segment) <= 255)):
                    backtrack(i + 1, path + [segment])
                    
        backtrack(0, [])
        return res
        