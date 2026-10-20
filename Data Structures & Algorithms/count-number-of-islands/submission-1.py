from collections import deque  
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_nodes = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    island_nodes.add((row,col))
        
        count = 0
        
        while island_nodes:
            node = island_nodes.pop()
            q = deque()
            q.append(node)
            while q:
                row, col = q.popleft()
                possible_neighbours = {(row-1, col), (row+1, col), (row, col-1), (row, col+1)}
                for p in possible_neighbours:
                    if p in island_nodes:
                        island_nodes.remove(p)
                        q.append(p)
            count += 1
        return count
            
            




        