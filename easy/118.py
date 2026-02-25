class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        
        for row in range(1, numRows + 1): 
            if row == 1:
                res.append([1])

            elif row == 2:
                res.append([1, 1])

            else:
                temp = [1] * (len(res[row - 2]) + 1)

                for i in range(1, len(temp) - 1):
                    temp[i] = res[row - 2][i - 1] + res[row - 2][i]

                res.append(temp)
            
        return res
