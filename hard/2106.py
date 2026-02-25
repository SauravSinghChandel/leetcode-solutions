class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        L = 0
        res = 0
        n = len(fruits)
        currSum = 0

        for R in range(n):
            currSum += fruits[R][1]

            while L <= R:
                Lpos = fruits[L][0]
                Rpos = fruits[R][0]
                # Checking if window is reachable
                if min(abs(Lpos - startPos), abs(Rpos - startPos)) + (Rpos - Lpos) <= k:
                    break

                else:
                    currSum -= fruits[L][1]
                    L += 1

            res = max(res, currSum)

        return res
        # left = []
        # right = []

        # for pos, val in fruits:
        #     if pos <= startPos:
        #         left.append([startPos - pos, val])
        #     else:
        #         right.append([pos - startPos, val])

        # left.reverse()

        # leftPrefix = [0]
        # rightPrefix = [0]

        # for _, val in left:
        #     leftPrefix.append(leftPrefix[-1] + val)
        
        # for _, val in right:
        #     rightPrefix.append(rightPrefix[-1] + val)
        # left = [d for d, _ in left]
        # right = [d for d, _ in right]
        # res = 0
        # def bisectHelper(arr, steps):
        #     return bisect.bisect_right(arr, steps)


        # for i in range(k + 1):
        #     # Left first
        #     leftCount = bisectHelper(left, i)
        #     rightCount = bisectHelper(right, k - 2 * i)

        #     res = max(res, leftPrefix[leftCount] + rightPrefix[rightCount])

        #     # then Right
        #     rightCount = bisectHelper(right, i)
        #     leftCount = bisectHelper(left, k - 2 * i)

        #     res = max(res, leftPrefix[leftCount] + rightPrefix[rightCount])

        # return res
