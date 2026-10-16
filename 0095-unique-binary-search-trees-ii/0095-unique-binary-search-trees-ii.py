class Solution:
    def generateTrees(self, n: int) -> list[TreeNode | None]:
        if n == 0:
            return []
            
        def helper(start, end):
            if start > end:
                return [None]
                
            all_trees = []
            for i in range(start, end + 1):
                left_trees = helper(start, i - 1)
                right_trees = helper(i + 1, end)
                
                for l in left_trees:
                    for r in right_trees:
                        curr = TreeNode(i)
                        curr.left = l
                        curr.right = r
                        all_trees.append(curr)
            return all_trees

        return helper(1, n)
        