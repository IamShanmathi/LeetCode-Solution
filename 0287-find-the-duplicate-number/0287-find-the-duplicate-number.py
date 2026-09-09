class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        # Find intersection
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # Find duplicate
        slow = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
        