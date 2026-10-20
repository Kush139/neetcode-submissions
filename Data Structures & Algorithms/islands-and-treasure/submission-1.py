class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    q.append((row,col))
        
        visited = set()
        while q:
            node = q.popleft()
            row, col = node
            possible_neighbours = {(row-1, col), (row+1, col), (row, col-1), (row, col+1)}
            for r, c in possible_neighbours:
                if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                    if grid[r][c] == 2147483647 and (r,c) not in visited:
                        grid[r][c] = grid[row][col] + 1
                        visited.add((r, c))
                        q.append((r, c))


        