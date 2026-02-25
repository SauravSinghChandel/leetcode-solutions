# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = []
        def dfs(node, pathMax):
            nonlocal res

            if not node:
                return

            pathMax = max(pathMax, node.val)

            if node.val >= pathMax:
                res.append(node.val)

            dfs(node.left, pathMax)
            dfs(node.right, pathMax)

        dfs(root, -float(inf))

        return len(res)
