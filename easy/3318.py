class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        def xSum(arr):
            arr = Counter(arr)
            n = len(arr.keys())

            if n < x:
                return sum(k * v for k, v in arr.items())
            return sum(k * v for k, v in sorted(arr.items(), key = lambda kv: (-kv[1], -kv[0]))[:x])

        return [xSum(nums[i:i + k]) for i in range(len(nums) - k + 1)]
