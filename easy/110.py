# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(node):

            if not node:
                return 0, True

            lheight, lbalanced = helper(node.left)
            rheight, rbalanced = helper(node.right)

            currHeight = 1 + max(rheight, lheight)
            currBalanced = abs(lheight - rheight) <= 1 and lbalanced and rbalanced

            return currHeight, currBalanced

        return helper(root)[1]
