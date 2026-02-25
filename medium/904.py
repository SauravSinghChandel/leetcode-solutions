class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = maxLen = 0
        fruitCount = defaultdict(int)
        n = len(fruits)
        for r in range(n):
            fruitCount[fruits[r]] += 1

            while len(fruitCount) > 2:
                fruitCount[fruits[l]] -= 1
                if fruitCount[fruits[l]] == 0:
                    del fruitCount[fruits[l]]
                l += 1

            maxLen = max(maxLen, r - l + 1)

        return maxLen
