class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        i = 0
        while i < n:
            if bits[i] == 0:
                i += 1
                res = True

            else:
                if i + 1 < n:
                    i += 2
                    res = False
                else:
                    i += 1
        return res
