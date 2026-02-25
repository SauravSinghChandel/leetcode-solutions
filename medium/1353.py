class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key = lambda e: e[0])
        h = []
        maxDay = max(e[1] for e in events)
        
        day = 1
        res = 0
        i = 0

        while day <= maxDay:

            while i < len(events) and events[i][0] == day:
                heapq.heappush(h, events[i][1])
                i += 1

            while h and h[0] < day:
                heapq.heappop(h)

            if h:
                heapq.heappop(h)
                res += 1

            day += 1

        return res
