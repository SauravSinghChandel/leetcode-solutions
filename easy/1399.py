class Solution:
    def countLargestGroup(self, n: int) -> int:
        def sum_digits(n):
            r = 0
            while n:
                r, n = r + n % 10, n // 10
            return r   

        total_count = dict()
        for i in range(1, 37):
            total_count[i] = 0
        
        for i in range(1, n+1):
            sum_digi = sum_digits(i)
            total_count[sum_digi] += 1

        max_value = max(total_count.values())

        count = 0

        for n in total_count.values():
            if n == max_value:
                count += 1

        return count
