class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitToNumber = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        res = []

        def backtrack(idx, substr):
            if len(digits) == 0:
                return
            if len(substr) == len(digits):
                res.append(substr)
                return

            for c in digitToNumber[digits[idx]]:
                
                backtrack(idx + 1, substr+c)


        backtrack(0, "")
        return res
