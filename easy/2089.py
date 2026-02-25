class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        less, tar, more = 0, 0, 0
        for i in nums:
            if i < target:
                less += 1
            elif i == target:
                tar += 1
            else:
                more += 1

        res = [i for i in range(less, less + tar)]
        return res
