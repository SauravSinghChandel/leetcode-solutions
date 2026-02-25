class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        mod = 10**9 + 7
        bit = 0
        powers = []
        while n > 0:
            if n & 1:
                powers.append(pow(2, bit, mod))
            bit += 1
            n >>= 1

        p_len = len(powers)
        prefix = [powers[0]]

        for i in range(1, p_len):
            prefix.append((prefix[-1] * powers[i]) % mod)
        
        inv_prefix = [0] * p_len
        inv_prefix[p_len - 1] = pow(prefix[p_len - 1], mod - 2, mod)

        for i in range(p_len - 1, 0, -1):
            inv_prefix[i - 1] = (inv_prefix[i] * powers[i]) % mod

        res = []
        for l, r in queries:
            if l > 0:
                prod = (prefix[r] * inv_prefix[l - 1]) % mod
            else:
                prod = prefix[r] % mod
            res.append(prod)

        return res
        # mod = 10 ** 9 + 7 
        # bit = 0
        # powers = []
        # while n > 0:
        #     if n & 1:
        #         powers.append(pow(2, bit, mod))

        #     bit += 1
        #     n >>= 1
        # prefix = [1]

        # for p in powers:
        #     prefix.append((prefix[-1] * p) % mod)

        # res = []

        # for l, r in queries:
        #     res.append((prefix[r + 1] * pow(prefix[l], mod - 2, mod)) % mod)

        # return res
        # res = []
        # n = str(bin(n))[2:]
        # mod = 10 ** 9 + 7
        # n = n[::-1]
        # powers = [2 ** i for i in range(len(n)) if n[i] != '0']
        
        # for q in queries:
        #     tot = 1

        #     for i in range(q[0], q[1] + 1):
        #         tot *= powers[i]
        #     res.append(tot % mod)
        #     tot = 1
        # return res
