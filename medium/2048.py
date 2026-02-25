class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        balanced = set()

        def dfs(i, selected):
            if  i == 8:
                if not selected:
                    return
                s = "".join(str(i) * i for i in selected)

                if len(s) <= 7:
                    for i in set(permutations(s)):
                        balanced.add(int("".join(i)))
                
                return
            dfs(i + 1, selected)
            dfs(i + 1, selected + [i])
        
        dfs(1, [])
        balanced = sorted(balanced)
        idx = bisect_right(balanced, n)
        return balanced[idx]

        return next(v for v in count(n + 1) if all(starmap(eq, Counter(map(int, str(v))).items())))
