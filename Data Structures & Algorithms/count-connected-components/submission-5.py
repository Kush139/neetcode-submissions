class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        visited = set()
        def dfs(node):
            if node in visited:
                return    
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    dfs(neighbour)
        count = 0
        for v in range(n):
            if v not in visited:
                dfs(v)
                count += 1
        return count

                
                     
                                    




        
        