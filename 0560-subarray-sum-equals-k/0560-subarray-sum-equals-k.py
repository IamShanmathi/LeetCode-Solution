class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum=0
        count=0
        seen={0:1}
        for num in nums:
            prefix_sum+=num
            needed= prefix_sum-k
            if needed in seen :
                count += seen[needed]
            if prefix_sum in seen:
                seen[prefix_sum] += 1
            else:
                seen[prefix_sum] = 1

        return count


                

        