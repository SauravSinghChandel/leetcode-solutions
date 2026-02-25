class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def hasZero(n):
            while n > 0:
                if n % 10 == 0:
                    return True
                n //= 10

            return False

        for i in range(1, n):
            a = i
            b = n - a

            if hasZero(a) or hasZero(b):
                continue
            
            return [a, b]
