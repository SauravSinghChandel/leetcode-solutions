class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        minVals = [0] * value

        for n in nums:
            minVals[n % value] += 1

        minVal = min(minVals)
        minIdx = minVals.index(minVal)

        return minVal * value + minIdx
        # res = defaultdict(int)

        # for num in nums:
        #     res[num % value] += 1

        # minVal = float('inf')
        # key = float('inf')
        # for r in range(value):
        #     count = res[r]

        #     if count < minVal:
        #         minVal = count
        #         key = r
        
        # return value * minVal + key
