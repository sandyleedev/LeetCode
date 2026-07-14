class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        num_rows, num_cols = len(heights), len(heights[0])
        p_queue, a_queue = deque(), deque()

        for r in range(num_rows):
            p_queue.append((r, 0))
            a_queue.append((r, num_cols - 1))
        
        for c in range(num_cols):
            p_queue.append((0, c))
            a_queue.append((num_rows - 1, c))
        
        def bfs(queue):
            reachable = set()
            while queue:
                (row, col) = queue.popleft()
                reachable.add((row, col))
                for (x,y) in [(1,0), (0,1), (-1, 0), (0, -1)]:
                    new_row, new_col = row + x, col + y
                    if new_row < 0 or new_row >= num_rows or new_col < 0 or new_col >= num_cols:
                        continue
                    if (new_row, new_col) in reachable:
                        continue
                    if heights[new_row][new_col] < heights[row][col]:
                        continue
                    queue.append((new_row, new_col))
            return reachable

        p_reachable = bfs(p_queue)
        a_reachable = bfs(a_queue)
        return list(p_reachable.intersection(a_reachable))