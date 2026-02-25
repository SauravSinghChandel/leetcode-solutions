class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = j = 0
        n, m = len(name), len(typed)

        while j < m:
            if i < n and name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0 and typed[j] == typed[j - 1]:
                j += 1
            else:
                return False
        
        return i == n
        # n, t = [], []

        # count = 1

        # name, typed = list(name), list(typed)

        # for i in range(1, len(name)):
        #     if name[i] == name[i - 1]:
        #         count += 1

        #     else:
        #         n.append((name[i - 1], count))
        #         count = 1
        # n.append((name[-1], count))
        # count = 1
        # for i in range(1, len(typed)):
        #     if typed[i] == typed[i - 1]:
        #         count += 1
        #     else:
        #         t.append((typed[i - 1], count))
        #         count = 1
        # t.append((typed[-1], count))
        
        # if len(n) != len(t):
        #     return False

        # for i in range(len(n)):

        #     if n[i][1] > t[i][1] or n[i][0] != t[i][0]:
        #         return False

        # return True
