# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')

        def max_gain(node):
            nonlocal max_sum
            if not node:
                return 0

            # Compute the maximum path sum going down left and right subtrees
            # Ignore negative paths by using max(..., 0)
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)

            # Price of a new path with 'node' as the highest node/peak
            current_path_sum = node.val + left_gain + right_gain
            max_sum = max(max_sum, current_path_sum)

            # Return the max sum the parent node can obtain by continuing this path
            return node.val + max(left_gain, right_gain)

        max_gain(root)
        return max_sum
        