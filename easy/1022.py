# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node, depth, currSum):
            nonlocal res
            currSum += str(node.val)
            if not node.left and not node.right:
                res += int(currSum, 2)
                return

            if node.left:
                dfs(node.left, depth + 1, currSum)
            if node.right:
                dfs(node.right, depth + 1, currSum)
        
        dfs(root, 0, '')
        return res
