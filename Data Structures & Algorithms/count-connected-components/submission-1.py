class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        #im thinking we count all the different groups by doing dfs. see the sizes. and then return  n -max(size). if we get a size thats >= n/2 we dont have to compute the rest

        #build adjacency list first
        graph = defaultdict(list)

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        visited = set()
        def bfs(node):
            q = deque([node])
            visiting = set()
            visiting.add(node)
            while q:
                v = q.popleft()
                for neighbour in graph[v]:
                    if neighbour not in visiting and neighbour not in visited:
                        q.append(neighbour)
                        visiting.add(neighbour)
                visited.add(v)
                visiting.remove(v)
        count = 0
        for v in range(n):
            if v not in visited:
                bfs(v)
                count += 1
        return count
                


        
        