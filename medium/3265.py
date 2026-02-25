class Solution:
    def countPairs(self, nums: List[int]) -> int:
        seen = defaultdict(int)
        res = 0
        nums.sort()
        for num in nums:
            s = list(str(num))

            visited = set()

            visited.add(num)
            sn = len(s)
            for i in range(sn):
                for j in range(i + 1, sn):
                    s[i], s[j] = s[j], s[i]
                    visited.add(int("".join(s)))
                    s[i], s[j] = s[j], s[i]
                    
            for v in visited:
                res += seen[v]

            seen[num] += 1

        return res
