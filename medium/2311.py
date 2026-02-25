class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        # res = ''

        # for i in range(len(s) - 1, -1, -1):

        #     if int(s[i] + res, 2) > k:
        #         continue

        #     res = s[i] + res

        # return len(res)
        val = 0
        count = 0
        power = 0
        n = len(s)

        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                count += 1

            else:
                if val + (1 << power) <= k:
                    val += 1 << power
                    count += 1

            power += 1

        return count
