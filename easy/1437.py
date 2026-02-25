class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev = 0
        n = len(nums)
        while prev < n and nums[prev] != 1:
            prev += 1

        for curr in range(prev + 1, n):
            if nums[curr] == 1:
                if curr - prev <= k:
                    return False
                prev = curr
            

        return True
