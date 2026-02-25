class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        tar = sum(apple)

        res = 0
        box = 0
        capacity.sort(reverse=True)
        for c in capacity:
            box += c
            res += 1
            if box >= tar:
                return res
