class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        return (m * n) // 2
        # if n == 1 and m == 1:
        #     return 0

        # def returnEvenOdd(n):
        #     even = 0
        #     odd = 0
        #     temp = n / 2
        #     if n % 2 == 0:
        #         even = math.ceil(temp)
        #         odd = math.floor(temp)
        #     else:
        #         even = math.floor(temp)
        #         odd = math.ceil(temp)

        #     return even, odd

        # ne, no = returnEvenOdd(n)
        # me, mo = returnEvenOdd(m)

        # return ne * mo + no * me
