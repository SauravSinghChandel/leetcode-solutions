class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        keys = [[n, k] for k, n in enumerate(nums)]
        keys = sorted(keys, key = lambda x : -x[0])[:k]

        return [x for x, k in sorted(keys, key = lambda x : x[1])]
        # res = []
        # if len(nums) == k:
        #     return nums
        
        # for key, num in enumerate(nums):
        #     if len(res) < k:
        #         heapq.heappush(res, (num, key))

        #     else:
        #         if num > res[0][0]:
        #             heapq.heappop(res)
        #             heapq.heappush(res, (num, key))

        # return [x for x, idx in sorted(res, key = lambda x : x[1])]
