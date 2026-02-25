class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        if sum(candidates) < target:
            return []

        def backtrack(start, path, total):

            if total == target:
                res.append(path.copy())
                return

            if total > target or start == len(candidates):
                return
            path.append(candidates[start])
            backtrack(start + 1, path, total + candidates[start])
            path.pop()

            while start + 1 < len(candidates) and candidates[start] == candidates[start + 1]:
                start += 1
            backtrack(start + 1, path, total)
        backtrack(0, [], 0)
        return res
