class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        ransomSet = set(ransomNote)

        for char in ransomSet:

            if ransomNote.count(char) > magazine.count(char):
                return False

        return True
