class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1
        x = 0
        
        if (n + 1) % 4 != 0:
            x = 1

        odd = 0

        for i in range(1, n, 2):
            odd ^= encoded[i]

        res = [odd ^ x]

        for e in encoded:
            res.append(res[-1] ^ e)
        
        return res
