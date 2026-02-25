class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.n1 = nums1
        self.n2 = nums2
        self.counter2 = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        old = self.n2[index]
        new = old + val
        self.counter2[old] -= 1
        if self.counter2[old] == 0:
            del self.counter2[old]
        self.counter2[new] += 1
        self.n2[index] = new

    def count(self, tot: int) -> int:
        res = 0

        for i in self.n1:
            diff = tot - i
            res += self.counter2.get(diff, 0)
        
        return res


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
