# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        path = []
        def bfs(root):
            if not root:
                return
            nonlocal path
            path.append(root.val)
            bfs(root.left)
            bfs(root.right)

        bfs(root)
        return path
