# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = root

        def dfs(root):
            nonlocal lca

            if not root:
                return
            
            lca = root

            if p is lca or q is lca:
                return

            if p.val > root.val and q.val > root.val:
                dfs(root.right)
            elif p.val < root.val and q.val < root.val:
                dfs(root.left)
            else:
                return

        dfs(root)
        return lca
