class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        n, m = len(players), len(trainers)

        players.sort()
        trainers.sort()

        res = 0
        i = j = 0
        while i < n and j < m:

            if players[i] <= trainers[j]:
                res += 1
                i += 1
            
            j += 1

        return res
