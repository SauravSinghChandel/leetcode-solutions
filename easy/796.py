class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        for i in range(len(s)):
            if s[i:] + s[:i] == goal:
                print(s[i:] + s[:i])
                return True

        return False
