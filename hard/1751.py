class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events = sorted(events, key = lambda x : x[0])
        n = len(events)
        res = 0
        dp = [[-1] * (k + 1) for _ in range(n)]

        next_events = [0] * n
        start_events = [event[0] for event in events]
        for i in range(n):
            next_events[i] = bisect.bisect_right(start_events, events[i][1])
        
        def attend_event(pos, k_remaining):
            if k_remaining == 0 or pos == n:
                return 0
            
            if dp[pos][k_remaining] != -1:
                return dp[pos][k_remaining]

            skip_event = attend_event(pos + 1, k_remaining)

            next_pos = next_events[pos]

            attended = attend_event(next_pos, k_remaining - 1) + events[pos][2]

            dp[pos][k_remaining] = max(skip_event, attended)

            return dp[pos][k_remaining]

        return attend_event(0, k)
