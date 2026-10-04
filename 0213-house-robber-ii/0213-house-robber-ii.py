class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        def rob_linear(arr):
            rob1, rob2 = 0, 0
            for n in arr:
                new_rob = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = new_rob
            return rob2
            
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
        