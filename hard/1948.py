class Solution:
    class TrieNode():
        def __init__(self, folder):
            self.folder = folder
            self.remove = False
            self.children = defaultdict()

    def insert(self, root, path):
        for s in path:
            if s not in root.children:
                root.children[s] = self.TrieNode(s)

            root = root.children[s]



    def markRepeating(self, root, visited):
        subfolders = []

        for childFolder, childNode in root.children.items():
            if childNode:
                subfolders.append(self.markRepeating(childNode, visited))

        key = ''.join(subfolders)

        if subfolders:
            if key in visited:
                visited[key].remove = True
                root.remove = True

            else:
                visited[key] = root

        return f"[{root.folder}{key}]"

    def savePath(self, root, curr_path, res):
        if root.remove:
            return

        curr_path.append(root.folder)
        res.append(curr_path[:])

        for childFolder, childNode in root.children.items():
            if childNode:
                self.savePath(childNode, curr_path, res)
        
        curr_path.pop()

    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = self.TrieNode("/")
        paths.sort()

        for path in paths:
            self.insert(root, path)

        visited = {}

        self.markRepeating(root, visited)

        res = []
        curr_path = []

        for childFolder, childNode in root.children.items():
            if childNode:
                self.savePath(childNode, curr_path, res)

        return res
