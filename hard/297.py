# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []

        if not root:
            return "[]"

        dq = deque([root])

        while dq:

            for _ in range(len(dq)):
                curr = dq.popleft()

                if not curr:
                    res.append('null')
                    continue

                res.append(str(curr.val))
                dq.append(curr.left)
                dq.append(curr.right)

        while res and res[-1] == 'null':
            res.pop()

        return "[" + ",".join(res) + "]"

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '[]':
            return None
        data = data[1:-1].split(',')

        root = TreeNode(data[0])

        dq = deque([root])
        i = 1

        while dq and i < len(data):

            parent = dq.popleft()

            val = data[i]
            parent.left = TreeNode(val) if val != 'null' else None
            if parent.left:
                dq.append(parent.left)
            i += 1

            if i < len(data):
                val = data[i]
                parent.right = TreeNode(val) if val != 'null' else None
                i += 1
                if parent.right:
                    dq.append(parent.right)

        return root

            

            


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
