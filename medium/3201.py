class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        even_count = sum(1 for i in nums if i % 2 == 0)
        odd_count = len(nums) - even_count
        same_parity_max = max(even_count, odd_count)

        alternating_len = 1
        prev_parity = nums[0] % 2

        for i in range(1, len(nums)):
            if nums[i] % 2 == prev_parity:
                continue

            alternating_len += 1
            prev_parity = nums[i] % 2

        return max(same_parity_max, alternating_len)
