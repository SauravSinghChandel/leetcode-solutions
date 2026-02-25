class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        n = len(arr)
        s = sum(arr)
        if s % 3 != 0:
            return False
        target = s // 3
        curr = 0
        parts = 0
        for i in range(n):
            curr += arr[i]

            if curr == target:
                parts += 1
                curr = 0

                if parts == 2 and i < n - 1:
                    return True

        return False
