class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        bank = [row.count('1') for row in bank]

        prev = 0
        res = 0

        for curr in bank:
            if curr != 0:
                res += curr * prev
                prev = curr
        
        return res
