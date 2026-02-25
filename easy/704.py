class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1


        while left < right:
            mid = left + (right - left) // 2
            print(mid, nums[mid])
            if target == nums[mid]:
                return mid

            if target > nums[mid]:
                left = mid + 1

            elif target < nums[mid]:
                right = mid

        if left == right:
            return left if nums[left] == target else -1
        return -1
