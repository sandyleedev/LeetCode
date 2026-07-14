class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        num_rows, num_cols = len(heights), len(heights[0])

        pac_queue = deque()
        atl_queue = deque()

        for i in range(num_rows):
            pac_queue.append((i, 0))
            atl_queue.append((i, num_cols - 1))
        
        for i in range(num_cols):
            pac_queue.append((0, i))
            atl_queue.append((num_rows - 1, i))
        
        def bfs(queue):
            reachable = set()
            while queue:
                (row, col) = queue.popleft()
                reachable.add((row, col))
                for (x, y) in [(1,0), (0, 1), (-1, 0), (0, -1)]:
                    new_row, new_col = row + x, col + y
                    # out of bounds checking
                    if new_row < 0 or new_row >= num_rows or new_col < 0 or new_col >= num_cols:
                        continue
                    if (new_row, new_col) in reachable:
                        continue
                    # checking new cell is higher / equal to
                    if heights[new_row][new_col] < heights[row][col]:
                        continue
                    queue.append((new_row, new_col))
            return reachable
        
        pac_reachable = bfs(pac_queue)
        atl_reachable = bfs(atl_queue)
        
        return list(pac_reachable.intersection(atl_reachable))
