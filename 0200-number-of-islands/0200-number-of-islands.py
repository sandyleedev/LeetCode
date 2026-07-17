class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        res = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    res += 1
                    grid[r][c] = "0"

                    neighbors = deque([(r, c)])
                    while neighbors:
                        row, col = neighbors.popleft()
                        for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                            new_row = dr + row
                            new_col = dc + col

                            if (0 <= new_row < len(grid)
                                and 0 <= new_col < len(grid[0])
                                and grid[new_row][new_col] == "1"):
                                    grid[new_row][new_col] = "0"
                                    neighbors.append((new_row, new_col))
        return res