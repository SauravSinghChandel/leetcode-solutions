class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        count = Counter(nums).items()

        return [k for k, v in count if v >= 2]
