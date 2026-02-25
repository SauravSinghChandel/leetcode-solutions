class Solution:
    def magicalSum(self, total_count: int, target_odd: int, numbers: List[int]) -> int:
        MOD = 10 ** 9 + 7
        
        @lru_cache(None)
        def dfs(remaining, odd_needed, index, carry):
            if remaining < 0 or odd_needed < 0 or remaining + carry.bit_count() < odd_needed:
                return 0
            if remaining == 0:
                return 1 if odd_needed == carry.bit_count() else 0
            if index >= len(numbers):
                return 0
            
            ans = 0
            for take in range(remaining + 1):
                ways = math.comb(remaining, take) * pow(numbers[index], take, MOD) % MOD
                new_carry = carry + take
                ans += ways * dfs(remaining - take, odd_needed - (new_carry % 2), index + 1, new_carry // 2)
                ans %= MOD
            return ans
        
        return dfs(total_count, target_odd, 0, 0)














        # n = len(nums)
        # mod = 10 ** 9 + 7
        # res = 0
        # fact = [1]

        # for i in range(1, m + 1):
        #     fact.append(fact[-1] * i % mod)


        # for seq in combinations_with_replacement(range(n), m):
        #     val = sum(1 << i for i in seq)
            
        #     if bin(val).count('1') == k:
        #         prod = 1

        #         for s in seq:
        #             prod = (prod * nums[s]) % mod

        #         count = Counter(seq)
        #         mult = fact[m]

        #         for c in count.values():
        #             mult //= factorial(c)

        #         res = (res + prod * mult) % mod

        # return res
