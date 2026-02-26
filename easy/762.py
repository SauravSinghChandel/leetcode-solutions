class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        res = 0
        prime = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}
        for i in range(left, right + 1):
            bitcount = i.bit_count()
            if bitcount in prime:
                res += 1

        return res
