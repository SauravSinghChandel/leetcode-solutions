class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        
        MOD = 10 ** 9 + 7

        groups = []
        count = 1

        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                count += 1
            else:
                groups.append(count)
                count = 1
        groups.append(count)

        total = 1

        for g in groups:
            total = (total * g)  % MOD

        if k <= len(groups):
            return total

        ps = [0] * k
        ps[0] = 1

        for g in groups:
            sum_ = 0
            dp = [0] * k

            for s in range(k):
                if s > 0:
                    sum_ = (sum_ + ps[s - 1] + MOD) % MOD

                if s > g:
                    sum_ = (sum_ - ps[s - g -1] + MOD) % MOD
                dp[s] = sum_

            ps = dp

        invalid = sum(ps[len(groups):]) % MOD

        return (total - invalid) % MOD
