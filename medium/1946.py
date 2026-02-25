class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        mutated = False
        num = list(num)
        n = len(num)

        for i in range(n):
            c = int(num[i])
            d = change[c]

            if c < d:
                num[i] = str(d)
                mutated = True

            elif c == d and mutated:
                num[i] = str(c)
            
            elif mutated:
                break

        return ''.join(num)
