class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        top3 = [(-1, -1)] * 3

        # Dummy insertions to accomodate 0th and n th slots
        startTime.append(eventTime)
        endTime.append(0)

        for i in range(len(startTime)):
            free_time = (startTime[i] - endTime[i - 1], i)

            if free_time[0] > top3[-1][0]:
                top3[-1] = free_time

                j = 2
                while j > 0:
                    if top3[j][0] > top3[j - 1][0]:
                        top3[j], top3[j-1] = top3[j-1], top3[j]
                    j -= 1
        res = 0
        for i in range(len(startTime) - 1):
            width = endTime[i] - startTime[i]
            free_time = 0
            for j in range(3):
                if width <= top3[j][0] and top3[j][1] not in {i, i+1}:
                    free_time = startTime[i + 1] - endTime[i - 1]
                    break

            if free_time == 0:
                free_time = startTime[i + 1] - endTime[i - 1] - width

            res = max(free_time, res)
        
        return res
