class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        # cycle detection but we just want to figure out when it becomes a cycle essentially 

        par = [i for i in range(len(edges)+1)]
        rank = [1] * (len(edges)+1)

        def find(x):
            print(x)
            if par[x] != x:
                #par[x] = par[par[x]]
                return find(par[x])
            else:
                return x
        
        def union(x,y):
            p1, p2 = find(x), find(y)

            if p1 == p2:
                return [x, y]
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return

        for x,y in edges:
            res = union(x,y)
            if res:
                return res

        
