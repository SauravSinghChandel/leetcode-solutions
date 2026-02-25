class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        wordList.append(beginWord)
        g = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                g[pattern].append(word)

        dq = deque([beginWord])
        visited = set([beginWord])

        res = 1

        while dq:

            for _ in range(len(dq)):
                word = dq.popleft()

                if word == endWord:
                    return res

                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]

                    for nei in g[pattern]:
                        if nei not in visited:
                            visited.add(nei)
                            dq.append(nei)
            res += 1
        return 0
