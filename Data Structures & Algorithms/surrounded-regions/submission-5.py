class Solution:
    def solve(self, board: List[List[str]]) -> None:
        border_o = set()

        ROWS, COLS = len(board), len(board[0])

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "O":
                    if row == 0 or row == ROWS-1 or col == 0 or col == COLS-1:
                        border_o.add((row, col))
        visited = set()
        def bfs(o):
            q = deque([o])
            visited.add(o)
            while q:
                r, c = q.popleft()
                possible_moves = {(r+1,c),(r-1,c), (r,c-1), (r,c+1)}
                for r, c in possible_moves:
                    if 0 <= r < ROWS-1 and 0 <= c < COLS and board[r][c] == 'O':
                        if (r,c) not in visited:
                            visited.add((r,c))
                            q.append((r,c))
        for b in border_o:
            if b not in visited:
                bfs(b)
        
        for row in range(ROWS):
            for col in range(COLS):
                if (row,col) not in visited:
                    board[row][col] = 'X'


                
