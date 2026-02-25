class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        l = 1
        r = x
        mid = x // 2
        mid2 = mid * mid
        res = 1

        while l <= r:
            mid = (r + l) // 2
            mid2 = mid * mid
            if mid2 == x:
                return mid

            if mid2 > x:
                r = mid - 1
            else:
                res = mid
                l = mid + 1
            
        return res
