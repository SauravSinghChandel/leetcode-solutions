from math import gcd

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        s = []
    
        for n in nums:
            s.append(n)

            while len(s) > 1:
                a, b = s[-2], s[-1]
                g = gcd(a, b)
                if g == 1:
                    break
                lcm = (a * b) // g
                s.pop()
                s[-1] = lcm

        return s
