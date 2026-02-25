class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        n = len(arr)
        right = n - 1
        # missing[i] = arr[i - 1] - (i + 1)
        # if arr[n - 1] - n < k:
        #     return k + n
        
        while left <= right:
            mid = (left + right) // 2

            missing_at_mid = arr[mid] - (mid + 1)

            if missing_at_mid < k:
                left = mid + 1
            else:
                right = mid - 1 

        return left + k
