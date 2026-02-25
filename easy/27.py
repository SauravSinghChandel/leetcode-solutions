class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        size = n

        for i in range(n):
            if nums[i] == val:
                nums[i] = 51
                size -= 1
            
        nums.sort()

        return size
