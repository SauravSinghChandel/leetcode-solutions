class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort(reverse=True)

        dp = {}
        longest_streak = 1
        
        for num in nums:
            dp[num] = dp.get(num * num, 0) + 1

            longest_streak = max(longest_streak, dp[num])

        return longest_streak if longest_streak > 1 else -1
