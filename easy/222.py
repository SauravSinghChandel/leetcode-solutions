# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        count = 0

        def inorder(root):
            nonlocal count
            if not root:
                return

            inorder(root.left)
            inorder(root.right)

            count += 1
        inorder(root)
        return count
