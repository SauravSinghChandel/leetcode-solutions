class Solution:
    def addDigits(self, num: int) -> int:
        return 1 + ((num - 1) % 9) if num > 0 else 0

        # while num > 9:
        #     num = sum(int(i) for i in str(num))
        # return num
