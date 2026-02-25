class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        res, l, r = 0, 0, 1
        visited = set()

        while r != len(s):
            visited.add(s[l])
            if s[r] not in visited:
                visited.add(s[r])

            else:
                l += 1
                r = l
                res = max(res, len(visited))
                visited.clear()

            r += 1
            res = max(res, len(visited))


        return(res)
