class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.taskInfo = {} # task -> (user, priority)
        self.heap = [] # (-priority, -taskId, taskId, userId)

        for u, t, p in tasks:
            self.taskInfo[t] = (u, p)
            heapq.heappush(self.heap, (-p, -t, -u))

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.taskInfo[taskId] = (userId, priority)
        heapq.heappush(self.heap, (-priority, -taskId, -userId))

    def edit(self, taskId: int, newPriority: int) -> None:
        userId, _ = self.taskInfo[taskId]
        self.taskInfo[taskId] = (userId, newPriority)
        heapq.heappush(self.heap, (-newPriority, -taskId, -userId))

    def rmv(self, taskId: int) -> None:
        del self.taskInfo[taskId]
        
    def execTop(self) -> int:
        while self.heap:
            p, t, u = heapq.heappop(self.heap)
            t = -t
            u = -u
            p = -p
            if t in self.taskInfo and p == self.taskInfo[t][1]:
                del self.taskInfo[t]
                return u

        return -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
