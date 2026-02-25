class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        def dfs(node, parent):
            if node in visited:
                return True

            visited.add(node)

            for nei in graph[node]:
                if nei != parent and dfs(nei, node):
                    return True

            return False

        for a, b in edges:
            visited = set()
            graph[a].append(b)
            graph[b].append(a)
            if dfs(a, b):
                return [a, b]

        return []
