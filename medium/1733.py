class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        lenLang = len(languages)
        langs = [set(l) for l in languages]

        candidates = set()
        
        for u, v in friendships:
            u, v = u - 1, v - 1

            if langs[u].isdisjoint(langs[v]):
                candidates.add(u)
                candidates.add(v)

        if not candidates:
            return 0
        freq = defaultdict(int)
        for person in candidates:
            for l in langs[person]:
                freq[l] += 1

        
        return len(candidates) - max(freq.values())
