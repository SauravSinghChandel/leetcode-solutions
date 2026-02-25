class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # def dist(p1):
        #     return ((p1[0]) ** 2 + (p1[1]) ** 2)

        # minHeap = []
        # res = []
        # for p in points:
        #     heapq.heappush(minHeap, (dist(p), p))

        # for _ in range(k):

        #     dist, p = heapq.heappop(minHeap)
        #     res.append(p)
        

        # return res
        points.sort(key = lambda p: (p[0] ** 2 + p[1] ** 2))
        return points[:k]
