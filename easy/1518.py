class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        totalMT = numBottles
        res = numBottles

        while totalMT >= numExchange:
            numBottles = totalMT // numExchange
            res += numBottles
            totalMT %= numExchange
            totalMT += numBottles

        return res
