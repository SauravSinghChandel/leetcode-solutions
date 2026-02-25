class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        unique = []
        prev = None

        for w in words:
            if not unique or sorted(w) != sorted(unique[-1]):
                unique.append(w)
                prev = w
            
        return unique
