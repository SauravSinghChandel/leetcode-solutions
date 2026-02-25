class Solution:
    def sortByBits(self, arr):
        temp = []
        for num in arr:
            ones = bin(num).count('1')
            temp.append((ones, num))
        temp.sort()
        result = []
        for pair in temp:
            result.append(pair[1])
        return result
