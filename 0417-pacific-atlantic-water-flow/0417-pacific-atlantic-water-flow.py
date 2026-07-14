class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        num_rows, num_cols = len(heights), len(heights[0])
        p_queue, a_queue = deque(), deque()

        # initialise
        for i in range(num_rows):
            p_queue.append((i, 0))
            a_queue.append((i, num_cols - 1))

        for i in range(num_cols):
            p_queue.append((0, i))
            a_queue.append((num_rows - 1, i))
        
        def bfs(queue):
            reachable = set()
            while queue:
                (row, col) = queue.popleft()
                reachable.add((row, col))

                for (x,y) in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    new_row, new_col = row + x, col + y
                    # 1) check if this is out of bound
                    if new_row < 0 or new_row >= num_rows or new_col < 0 or new_col >= num_cols:
                        continue
                    # 2) check if this is already in the set
                    if (new_row, new_col) in reachable:
                        continue
                    # 3) check if this coordinate is not higher or equal (lower than the current cell)
                    if heights[new_row][new_col] < heights[row][col]:
                        continue
                    # 4) if it's not, we can add it to the reachable set!
                    queue.append((new_row, new_col))
            return reachable

        p_reachable = bfs(p_queue)
        a_reachable = bfs(a_queue)

        return list(p_reachable.intersection(a_reachable))