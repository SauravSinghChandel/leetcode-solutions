class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()

        size = len(nums)

        if size == 1:
            return 0
        minimum = float(inf)

        for i in range(size - k + 1):
            track = abs(nums[i] - nums[i+k-1])
            minimum = min(track, minimum)

        return minimum
