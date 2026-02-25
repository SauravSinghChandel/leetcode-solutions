class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 0, self.n - 1, 1)
    
    def build(self, arr, l, r, node):
        if l == r:
            self.tree[node] = arr[l]
            return
        
        mid = (l + r) // 2
        self.build(arr, l, mid, 2 * node)
        self.build(arr, mid + 1, r, 2 * node + 1)

        self.tree[node] = max(self.tree[node * 2], self.tree[2 * node + 1])

    def update(self, idx, value, l, r, node):

        if l == r:
            self.tree[node] = value
            return

        mid = (l + r) // 2

        if idx <= mid:
            self.update(idx, value, l, mid, node * 2)
        else:
            self.update(idx, value, mid + 1, r, node * 2 + 1)

        self.tree[node] = max(self.tree[node * 2], self.tree[2 * node + 1])

    def query(self, value, l, r, node):
        if self.tree[node] < value:
            return -1
        
        if l == r:
            return l

        mid = (l + r) // 2

        if self.tree[node * 2] >= value:
            return self.query(value, l, mid, node * 2)
        else:
            return self.query(value, mid + 1, r, node * 2 + 1)

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        st = SegmentTree(baskets)

        unplaced = 0

        for fruit in fruits:
            idx = st.query(fruit, 0, st.n - 1, 1)

            if idx == -1:
                unplaced += 1

            else:
                st.update(idx, -1, 0, st.n - 1, 1)

        return unplaced
