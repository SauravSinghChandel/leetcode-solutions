class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)

        for course, prereq in prerequisites:
            graph[course].append(prereq)

        visited = [0] * numCourses
        res = []
        
        def dfs(course):

            if visited[course] == 1:
                return False

            if visited[course] == 2:
                return True

            visited[course] = 1

            for pre in graph[course]:
                if not dfs(pre):
                    return False

            visited[course] = 2
            res.append(course)
            return True

        
        for course in range(numCourses):
            if not dfs(course):
                return []

        return res
