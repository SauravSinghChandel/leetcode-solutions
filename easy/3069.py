class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = []
        arr2 = []

        for i in range(len(nums)):

            if i == 0 or i == 1:
                if i % 2 == 0:
                    arr1.append(nums[i])

                else:
                    arr2.append(nums[i])

            else:
                if arr1[-1] > arr2[-1]:
                    arr1.append(nums[i])
                else:
                    arr2.append(nums[i])

        arr1.extend(arr2)
        return arr1
