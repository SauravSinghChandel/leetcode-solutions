class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}

        bucketSort = [[] for i in range(len(nums) + 1)]

        for i in nums:
            count[i] = 1 + count.get(i, 0)

        for n, c in count.items():
            bucketSort[c].append(n)

        res = []
        for i in range(len(bucketSort) - 1, 0, -1):
            for n in bucketSort[i]:
                res.append(n)

                if len(res) == k:
                    return res
        return res
