from collections import deque, defaultdict
import bisect

class Router:
    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        self.queue = deque()  # stores (s, d, t)
        self.seen = set()     # for duplicate detection
        self.destMap = defaultdict(list)  # destination -> sorted timestamps

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        key = (source, destination, timestamp)
        if key in self.seen:
            return False

        # Evict oldest if at capacity
        if len(self.queue) == self.memoryLimit:
            old_s, old_d, old_t = self.queue.popleft()
            self.seen.remove((old_s, old_d, old_t))
            # remove old_t from destination list
            lst = self.destMap[old_d]
            idx = bisect.bisect_left(lst, old_t)
            lst.pop(idx)

        # Add new packet
        self.queue.append(key)
        self.seen.add(key)
        self.destMap[destination].append(timestamp)  # increasing order guaranteed
        return True

    def forwardPacket(self) -> list[int]:
        if not self.queue:
            return []
        s, d, t = self.queue.popleft()
        self.seen.remove((s, d, t))
        # remove from destMap
        lst = self.destMap[d]
        idx = bisect.bisect_left(lst, t)
        lst.pop(idx)
        return [s, d, t]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        lst = self.destMap[destination]
        # count timestamps in [startTime, endTime]
        left = bisect.bisect_left(lst, startTime)
        right = bisect.bisect_right(lst, endTime)
        return right - left
