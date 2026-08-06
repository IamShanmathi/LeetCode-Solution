class Solution:
    def maxPower(self, s: str) -> int:
        count=1
        maximum=1
        for i in range(len(s)-1):
            if s[i] ==  s[i+1]:
                count+=1
                maximum=max(count,maximum)
            else:
                count=1
        return maximum

            

        