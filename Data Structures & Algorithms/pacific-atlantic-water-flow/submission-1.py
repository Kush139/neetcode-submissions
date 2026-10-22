class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        pacific = set()
        atlantic = set()

        ROWS, COLS = len(heights), len(heights[0])

        for r in range(ROWS):
            pacific.add((r, 0))
            atlantic.add((r, COLS - 1))

        for c in range(COLS):
            pacific.add((0, c))
            atlantic.add((ROWS - 1, c))
        
        def bfs(flow):
            q = deque(flow)
            visited = set()
            while q:
                r, c = q.popleft()
                visited.add((r,c))
                possible_moves = {(r+1,c), (r-1,c), (r, c+1), (r, c-1)}
                for row, col in possible_moves:
                    if 0 <= row < ROWS and 0 <= col < COLS and heights[row][col] >= heights[r][c]:
                        if (row, col) not in visited:
                            q.append((row,col))
                            visited.add((row, col))
            return visited
        
        v_pac = bfs(pacific)
        v_atl = bfs(atlantic)

        res = []

        for coord in v_pac:
            if coord in v_atl:
                res.append(coord)
        return res



    

    
    

