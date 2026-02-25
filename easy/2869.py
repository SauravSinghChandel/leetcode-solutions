class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        visited = set()
        rangeMax = k
        count = 0
        while k > 0:
            a = nums.pop()
            count += 1
            if a <= rangeMax and a not in visited:
                visited.add(a)
                k -= 1
            
        return count
