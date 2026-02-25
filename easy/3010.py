class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        res = nums[0]
        nums = nums[1:]
        heapq.heapify(nums)
        for _ in range(2):
            res += heapq.heappop(nums)
        return res
