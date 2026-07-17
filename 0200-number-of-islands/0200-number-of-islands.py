class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        num_rows = len(grid)
        num_cols = len(grid[0])

        num_islands = 0

        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == "1":
                    num_islands += 1
                    grid[r][c] = "0"
                    q = deque([(r, c)])
                    while q:
                        row, col = q.popleft()
                        for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            new_row = row + x
                            new_col = col + y
                            if (0 <= new_row < num_rows
                                and 0 <= new_col < num_cols
                                and grid[new_row][new_col] == "1"
                            ):
                                grid[new_row][new_col] = "0"
                                q.append((new_row, new_col))
        
        return num_islands