class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count={}
        for num in nums:
            if num in count:
                count[num]+=1
            else:
                count[num]=1
        repeated =0
        missing=0
        for num in range(1,len(nums)+1):
            if num not in count:
                missing=num
            elif count[num]==2:
                repeated=num
        return[repeated,missing]

        