class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr) // 2
        t = 0
        res = 0
        for k, v in Counter(arr).most_common():
            t += v
            res += 1
            if t >= n:
                return res
