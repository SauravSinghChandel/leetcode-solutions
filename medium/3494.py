class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n, m = len(skill), len(mana)

        times = [0] * n

        for j in range(m):
            currTime = 0
            for i in range(n):
                currTime = max(currTime, times[i]) + skill[i] * mana[j]

            times[-1] = currTime

            for i in range(n - 2, -1, -1):
                times[i] = times[i + 1] - skill[i + 1] * mana[j]

        return times[-1]









        n, m = len(skill), len(mana)

        times = [0] * n

        for j in range(m):
            currTime = 0

            for i in range(n):
                currTime = max(currTime, times[i]) + skill[i] * mana[j]

            times[-1] = currTime

            for i in range(n - 2, -1, -1):
                times[i] = times[i + 1] - skill[i + 1] * mana[j]

        return times[-1]
