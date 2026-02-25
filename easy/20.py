class Solution(object):
    def isValid(self, s):
        open = ["(", "{", "["]
        close = [")", "}", "]"]
        open_close = {"(" : ")", "{" : "}", "[" : "]"}

        stack = []

        for i in s:

            if i in open:

                stack.append(i)

            elif i in close and stack == []:
                return False

            elif open_close[stack[-1]] != i:
                return False

            else:
                if open_close[stack[-1]] == i:
                    stack.pop()

                

        if len(stack) == 0:
            return True

        else: 
            return False
