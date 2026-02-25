class Solution:
    def kMirror(self, k: int, n: int) -> int:

        def baser(n):
            base_k = []
            while n >= 1:
                base_k.append(n % k)
                n //= k

            return base_k

        def isPalindrome(l):
            return l == l[::-1]

        count = 0
        res = 0
        length = 1
        while count < n:

            for i in range(10**(length - 1), 10 ** (length)):
                num = str(i)
                num = int(num + num[-2::-1])

                if isPalindrome(baser(num)):
                    count += 1
                    res += num
                    if count == n: return res

            for i in range(10**(length - 1), 10 ** (length)):
                num = str(i)
                num = int(num + num[::-1])

                if isPalindrome(baser(num)):
                    count += 1
                    res += num
                    if count == n: return res

            length += 1
            

        return res
