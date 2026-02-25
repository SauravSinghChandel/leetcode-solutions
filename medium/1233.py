class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        res = [folder[0]]

        n = len(folder)

        for i in range(1, n):
            if not folder[i].startswith(res[-1] + "/"):
                res.append(folder[i])

        return res
