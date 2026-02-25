class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        freq = [0] * 101
        offset = 50
        n = len(nums)
        res = []

        for i in range(k):
            freq[nums[i] + offset] += 1

        def getSmallest():
            count = 0

            for v in range(101):
                count += freq[v]
                if count >= x:
                    return v - offset if v - offset < 0 else 0

            return 0
        
        res.append(getSmallest())

        for i in range(k, n):
            freq[nums[i] + offset] += 1
            freq[nums[i - k] + offset] -= 1
            res.append(getSmallest())

        return res
