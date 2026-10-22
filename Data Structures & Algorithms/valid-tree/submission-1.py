class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        visiting = set()

        def dfs(node, parent=None):
            if node in visiting:
                return False
            visiting.add(node)
            for neighbour in graph[node]:
                if neighbour != parent and not dfs(neighbour, node):
                    return False
            visiting.remove(node)
            return True

            # 0 : {1}, 1:{0,2,3,4}, 2: {1, 3}, 3 {1,2}, 4: [1]

            # 0: 1 1: 0 2: 3 3: 2
            


        # run dfs and do cycle detection. also wanna make sure all nodes are connected

        for i in range(n):
            if not dfs(i):
                return False
        if len(edges) != n-1:
            return False
        return True

        