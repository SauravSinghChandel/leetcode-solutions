class Solution:
    def minNode(self, root: TreeNode) -> TreeNode:
        curr = root

        while  curr and curr.left:
            curr = curr.left

        return curr

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        
        if not root:
            return None
        

        if key > root.val:
            root.right = self.deleteNode(root.right, key)

        elif key < root.val:
            root.left = self.deleteNode(root.left, key)


        else:
            if not root.left:
                return root.right

            elif not root.right:
                return root.left
            
            else:
                min_node = self.minNode(root.right)
                root.val = min_node.val
                root.right = self.deleteNode(root.right, min_node.val)

        return root
