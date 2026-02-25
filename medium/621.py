class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:


        count = Counter(tasks)
        max_freq = max(count.values())
        freq = list(count.values())
        max_freq_ele = 0

        for i in freq:
            if i == max_freq:
                max_freq_ele += 1

        slot_size = n + 1

        return max(slot_size * (max_freq - 1) + max_freq_ele, len(tasks))
        # count = Counter(tasks)

        # maxHeap = [ -cnt for cnt in count.values()]

        # heapq.heapify(maxHeap)

        # dq = deque()
        # t = 0

        # while maxHeap or dq:
        #     t += 1

        #     if maxHeap:
        #         task = 1 + heapq.heappop(maxHeap)
        #         if task:
        #             dq.append((task, t + n))

        #     if dq and dq[0][1] == t:
        #         heapq.heappush(maxHeap, dq.popleft()[0])

        # return t
