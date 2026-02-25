class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        n = Counter(nums)

        for k, v in n.items():
            if v > 2:
                return False

        return True
