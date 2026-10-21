class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(set)
        path = set()
        completed = set()

        for p in prerequisites:
            graph[p[0]].add(p[1])
        
        def dfs(course):
            if course in path:
                return False
            if course in completed:
                return True
            path.add(course)
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            path.remove(course)
            completed.add(course)
            return True

        for course in range(numCourses):
            if not dfs(course): 
                return False
        return True
    

             
        