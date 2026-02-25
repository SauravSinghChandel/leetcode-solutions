class Solution:
    def longestPalindrome(self, s: str) -> int:
        import collections

        count = collections.Counter(s)

        odd = False
        total = 0
        for key, value in count.items():
            print(key, value)
            if value % 2 == 0:
                print(value)
                total += value
            else:
                total += value - 1
                odd = True
        if odd:
            total += 1
        return total
