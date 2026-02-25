class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        def toMins(t):
            h, m = map(int, t.split(":"))

            return h * 60 + m

        s1, e1 = map(toMins, event1)
        s2, e2 = map(toMins, event2)

        return s1 <= e2 and s2 <= e1
