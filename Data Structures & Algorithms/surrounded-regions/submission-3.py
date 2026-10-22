class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #kind of like islands question
        #but if part of island is touching border, dont capture it. else capture

        o = set()

        ROWS, COLS = len(board), len(board[0])

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "O":
                    o.add((row, col))
        visited_global = set()
        def bfs(coord):
            q = deque([coord])
            visited = set()
            capture = True
            visited.add(coord)
            while q:
                r, c = q.popleft()
                if r == 0 or r == ROWS-1 or c == 0 or c == COLS-1:
                    capture = False
                visited_global.add((r,c))
                possible_moves = {(r+1,c),(r-1,c), (r,c-1), (r,c+1)}
                for row, col in possible_moves:
                    if 0 <= row < ROWS and 0 <= col < COLS and (row,col) not in visited:
                        if board[row][col] == "O":
                            visited.add((row,col))
                            q.append((row,col))
            if capture:
                for row, col in visited:
                    board[row][col] = 'X'
                        

        for coord in o:
            if coord not in visited_global:
                bfs(coord)


        