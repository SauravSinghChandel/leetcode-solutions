class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
    
        for i in range(-3, -len(cost) - 1, -1):
            print(i)
            cost[i] += min(cost[i+2], cost[i+1])

        return min(cost[0], cost[1])
