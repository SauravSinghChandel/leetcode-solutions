class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        res = numBottles

        MTbottles = numBottles

        while MTbottles >= numExchange:
            numExchange += 1
            MTbottles -= numExchange - 2

            res += 1

        return res
