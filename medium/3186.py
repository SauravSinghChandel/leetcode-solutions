class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        count = Counter(power)
        vec = [(-10**9, 0)]
        for p in sorted(count.keys()):
            vec.append((p, count[p]))

        n = len(vec)
        f = [0] * n

        j = 1
        mx = 0
        for i in range(n):

            while j < i and vec[i][0] - 2 > vec[j][0]:
                mx = max(f[j], mx)
                j += 1

            f[i] = mx + vec[i][0] * vec[i][1]

        return max(f)
