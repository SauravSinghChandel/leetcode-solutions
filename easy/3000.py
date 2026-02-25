class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        maxDiag = max(l ** 2 + b ** 2 for l, b in dimensions)
        res = max(l * b for l, b in dimensions if l ** 2 + b ** 2 == maxDiag)
        return res
        # res = []

        # for l, b in dimensions:
        #     n = (math.sqrt((l ** 2) + (b ** 2)), l * b)

        #     res.append(n)

        # res.sort(reverse=True)
        # return res[0][-1]
