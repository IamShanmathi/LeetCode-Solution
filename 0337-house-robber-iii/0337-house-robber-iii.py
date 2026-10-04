# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode | None) -> int:
        def dfs(node):
            if not node:
                return [0, 0]
                
            left_pair = dfs(node.left)
            right_pair = dfs(node.right)
            
            # If we rob this node, we cannot rob its children
            with_root = node.val + left_pair[1] + right_pair[1]
            
            # If we don't rob this node, we choose max from each child branch
            without_root = max(left_pair) + max(right_pair)
            
            return [with_root, without_root]
            
        return max(dfs(root))
        