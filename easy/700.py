# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:

    def printBST(self, root, res = []):
        queue = deque()
        queue.append(root)
        while len(queue) > 0:

            for i in range(len(queue)):
                curr = queue.popleft()
                res.append(curr.val)
                if curr.left:
                    queue.append(curr.left)

                if curr.right:
                    queue.append(curr.right)

        return res
                    
        

    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return None

        if val == root.val:
            print(root)
            return root

        if val < root.val:
            return self.searchBST(root.left, val)

        elif val > root.val:
            return self.searchBST(root.right, val)
