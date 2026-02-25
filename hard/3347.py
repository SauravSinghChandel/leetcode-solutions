class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        
        count = Counter(nums)
        presum = defaultdict(int)

        for x in count:
            presum[x - k] += count[x]
            presum[x + k + 1] -= count[x]

        keys = sorted(count.keys() | presum.keys())
        res = total = 0
        for x in keys:
            total += presum[x]
            ops = min(total - count[x], numOperations)
            res = max(res, count[x] + ops)

        return res
