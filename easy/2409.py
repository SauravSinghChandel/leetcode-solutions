class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        def con(start, end):
            daysBefore= [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
            days = []
            startDay = int(daysBefore[int(start[:2]) - 1]) + int(start[3:])
            endDay = int(daysBefore[int(end[:2]) - 1]) + int(end[3:])
            return [startDay, endDay]

        a, b = con(arriveAlice, leaveAlice), con(arriveBob, leaveBob)

        return max(0, min(a[1], b[1]) - max(a[0], b[0]) + 1)
