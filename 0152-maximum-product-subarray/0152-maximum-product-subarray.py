class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res = nums[0]
        cur_min, cur_max = 1, 1
        
        for n in nums:
            if n == 0:
                cur_min, cur_max = 1, 1
                res = max(res, 0)
                continue
                
            # Temporarily store cur_max * n because cur_max gets updated in the next line
            tmp = cur_max * n
            cur_max = max(n * cur_max, n * cur_min, n)
            cur_min = min(tmp, n * cur_min, n)
            
            res = max(res, cur_max)
            
        return res
        