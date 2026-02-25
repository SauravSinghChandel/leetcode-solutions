class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n = len(s)

        # def applyA(s):
        #     n = len(s)
        #     s = list(s)

        #     for i in range(1, n, 2):
        #         s[i] = str((int(s[i]) + a) % 10)

        #     return ''.join(s)

        # def applyB(s):
        #     s = deque(s)
            
        #     for _ in range(b):
        #         s.appendleft(s.pop())

        #     return "".join(s)

        visited = set()
        q = deque([s])
        smallest = s
        visited.add(s)
        while q:
            curr = q.popleft()
            smallest = min(smallest, curr)
            
            sC = list(curr)
            for i in range(1, n, 2):
                sC[i] = str((int(sC[i]) + a) % 10)

            sA = "".join(sC)

            if sA not in visited:
                visited.add(sA)
                q.append(sA)
            
            sB = curr[-b:] + curr[:-b]
            if sB not in visited:
                visited.add(sB)
                q.append(sB)
            
        return smallest


        # def dfs(s):
        #     nonlocal visited
        #     if s in visited:
        #         return
        #     visited.add(s)

        #     dfs(applyA(s))
        #     dfs(applyB(s))


        # dfs(s)
        return min(visited)
