class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    q.append((row,col))
                if grid[row][col] == 1:
                    fresh += 1
        minutes = 0
        while q:
            fresh_nei = False
            for  i in range(len(q)):
                row, col = q.popleft()
                possible_neighbours = {(row-1, col), (row+1, col), (row, col-1), (row, col+1)}
                for r, c in possible_neighbours:
                    if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                        if grid[r][c] == 1:
                            fresh_nei = True
                            grid[r][c] = 2
                            q.append((r, c)) 
                            fresh -= 1  
            if fresh_nei:
                minutes += 1
        if not fresh:
            return minutes
        return -1   