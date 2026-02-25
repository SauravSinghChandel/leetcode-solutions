class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []

        subset = []

        def backtrack(i):

            if i >= len(s):
                res.append(subset[:])
                return

            for j in range(i+1, len(s)+1):
                substr = s[i:j]
                
                if substr == substr[::-1]:
                    subset.append(s[i:j])
                    backtrack(j)
                    subset.pop()

        backtrack(0)

        return res
