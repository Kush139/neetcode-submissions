class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        island_nodes = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    island_nodes.add((row, col))

        max_area = 0
        while island_nodes:
            node = island_nodes.pop()
            q = deque()
            q.append(node)
            area = 1
            while q:
                row, col = q.popleft()
                possible_neighbours = {(row-1, col), (row+1, col), (row, col-1), (row, col+1)}
                for p in possible_neighbours:
                    if p in island_nodes:
                        area += 1
                        island_nodes.remove(p)
                        q.append(p)
            max_area = max(max_area, area)
        return max_area

        