class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        time = 0

        for i in range(len(points) - 1):
            curr = points[i]
            curr_next = points[i + 1]

            dx = curr_next[0] - curr[0]
            dy = curr_next[1] - curr[1]

            time += max(abs(dx), abs(dy))

        return time
