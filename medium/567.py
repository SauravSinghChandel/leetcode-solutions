class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False

        s1 = Counter(s1)

        l = 0
        counter = {}
        for r in range(m):
            if s2[r] not in s1:
                l = r + 1
                counter = {}
                continue
            
            if s2[r] not in counter:
                counter[s2[r]] = 0

            counter[s2[r]] += 1

            if counter[s2[r]] > s1[s2[r]]:
                while counter[s2[r]] > s1[s2[r]]:
                    counter[s2[l]] -= 1
                    l += 1

            if counter == s1:
                return True

        return False
