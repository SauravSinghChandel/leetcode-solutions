class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        freq = [0] * n
        freeRooms = [i for i in range(n)]
        occupiedRooms = []
        heapq.heapify(freeRooms)
        heapq.heapify(occupiedRooms)

        for start, end in meetings:

            while occupiedRooms and occupiedRooms[0][0] <= start:
                time, room = heapq.heappop(occupiedRooms)
                heapq.heappush(freeRooms, room)

            if freeRooms:
                room = heapq.heappop(freeRooms)
                freq[room] += 1
                availTime = end
                heapq.heappush(occupiedRooms, (availTime, room))
            else:
                time, room = heapq.heappop(occupiedRooms)
                freq[room] += 1
                availTime = time + (end - start)
                heapq.heappush(occupiedRooms, (availTime, room))

        return freq.index(max(freq))
