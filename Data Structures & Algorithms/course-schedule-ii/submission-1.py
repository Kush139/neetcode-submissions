class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        path = set()
        complete = set()
        res = []


        #[[1, 0], [2, 1], [3,2], [5, 4]]
        # {1: [0], 2: [1], 3: [2]}
        # {1: [0], 2: [1, 0], 3:[2, 1, 0], 5:[4]}
        for course in prerequisites:
            graph[course[0]].append(course[1])
        
        def dfs(course):
            if course in path:
                return False
            if course in complete:
                return True
            path.add(course)
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            path.remove(course)
            complete.add(course)
            res.append(course)
            return True
        for course in range(numCourses):
            if not dfs(course):
                return []
        return res





        