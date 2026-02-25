class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        dqf, dqb = deque(fruits), deque(baskets)
        res = 0
        
        while dqf and dqb:
            placed = False
            for basket in dqb:
                if dqf[0] > basket:
                    continue
                else:
                    placed = True
                    dqb.remove(basket)
                    break
                
            if not placed:
                res += 1
            dqf.popleft()

        return res
