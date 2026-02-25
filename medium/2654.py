class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Step 1: check global gcd
        g = nums[0]
        for num in nums[1:]:
            g = gcd(g, num)
        if g > 1:
            return -1
        
        # Step 2: if there's already a 1
        ones = nums.count(1)
        if ones > 0:
            return n - ones
        
        # Step 3: find shortest subarray with gcd == 1
        min_len = n + 1
        for i in range(n):
            g = nums[i]
            for j in range(i + 1, n):
                g = gcd(g, nums[j])
                if g == 1:
                    min_len = min(min_len, j - i + 1)
                    break  # stop early (gcd can't get smaller than 1)
        
        # Step 4: compute total operations
        return (min_len - 1) + (n - 1)
