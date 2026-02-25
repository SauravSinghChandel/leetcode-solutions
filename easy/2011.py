class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res = 0
        for k, v in Counter(operations).items():
            if k[1] == "+": 
                res += v
            else:
                res -= v

        return res
