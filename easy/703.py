class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)

        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        return self.minHeap[0]
        
    # def heapify(self, heap):

    #     curr = (len(heap) - 1) // 2

    #     while curr > 0:
    #         i = curr

    #         while (2 * i) < len(heap):
    #             if (2 * 1 + 1 < len(heap) and heap[2 * i] < heap[2 * i + 1] and heap[i] < heap[2 * i + 1]):
    #                 heap[i], heap[ 2 * i + 1] = heap[2 * i + 1], heap[i]

    #                 i = 2 * i + 1

    #             elif heap[i] < heap[2 * i]:
    #                 heap[i], heap[2*i] = heap[2*i], heap[i]

    #                 i *= 2

    #             else:
    #                 break

    #         curr -= 1

    #     return heap



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
