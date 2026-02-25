class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        count = dict()
        
        def counter(listing: list):
            listing = listing.split(" ")
            for i in listing:
                if i in count:
                    count[i] += 1
                else:
                    count[i] = 1

        counter(s1)
        counter(s2)
        result = []
        for i in count:
            if count[i] == 1:
                result.append(i)
        return result
