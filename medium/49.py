from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        
        hMap = defaultdict(list)

        for s in strs:

            count = [0] * 26

            for c in s:

                count[ord(c) - ord("a")] += 1

            hMap[tuple(count)].append(s)

        return hMap.values()
