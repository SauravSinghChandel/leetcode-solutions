class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def count_le(x):

            count = 0

            for i in nums1:
                if i > 0:
                    count += bisect_right(nums2, x / i)

                elif i < 0:
                    count += len(nums2) - bisect_left(nums2, math.ceil(x / i))

                else:
                    if x >= 0:
                        count += len(nums2)

            return count


        low, high = -10**10 - 1, 10**10 + 1
        res = high

        while low < high:

            mid = (high + low) // 2

            if count_le(mid) >= k:
                res = mid
                high = mid

            else:
                low = mid + 1

        return res
