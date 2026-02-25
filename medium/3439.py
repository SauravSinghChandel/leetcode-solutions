class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        free_time = []
        n = len(startTime)
        if startTime[0] != 0:
            free_time.append(startTime[0])            
        
        for i in range(1, n):
            if startTime[i] >= endTime[i - 1]:
                free_time.append(startTime[i] - endTime[i - 1])

        if endTime[n - 1] != eventTime:
            free_time.append(eventTime - endTime[n - 1])

        print(free_time)

        if len(free_time) <= k:
            return sum(free_time)

        win = sum(free_time[:k+1])
        res = win

        for i in range(k + 1, len(free_time)):
            win += free_time[i] - free_time[i - (k+1)]
            res = max(res, win)
        return res
