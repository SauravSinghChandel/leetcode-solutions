class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        res = ""

        candidate = sorted([c for c, w in Counter(s).items() if w >= k], reverse=True)

        q = deque(candidate)

        while q:
            curr = q.popleft()

            if len(curr) > len(res):
                res = curr

            for ch in candidate:
                nxt = curr + ch
                it = iter(s)

                if all(c in it for c in nxt * k):
                    q.append(nxt)

        return res
