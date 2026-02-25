class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        count = [0, 0] # count[0] = Num of 0's & count[1] = Num of 1's
        ans = 0

        l = 0

        for r, c in enumerate(s):
            count[int(c)] += 1

            while count[0] > k and count[1] > k:
                count[int(s[l])] -= 1
                l += 1

            ans += r - l + 1

        return ans
