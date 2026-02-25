class Solution:
    def maximum69Number (self, num: int) -> int:
        n = list(str(num))

        for s in range(len(n)):
            if n[s] == "6":
                n[s] = "9"
                break

        return int("".join(n))
