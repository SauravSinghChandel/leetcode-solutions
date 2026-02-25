
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)
        stack = [] #pair: index, temp   

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                stackInd, stackT = stack.pop()
                res[stackInd] = i - stackInd

            stack.append([i, t])

        return res
