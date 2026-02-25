class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        res = 0
        if num2 == 0: return res
        while num1 > 0:
            if num1 < num2:
                num1, num2 = num2, num1
            
            num1 = num1 - num2
            res += 1

        return res
