class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: return False

        adj = [[] for _ in range(n)]
        for A, B in edges:
            adj[A].append(B)
            adj[B].append(A)
        
        seen = set()

        def dfs(node, parent):
            if node in seen:
                return
            seen.add(node)
            for nei in adj[node]:
                if nei == parent:
                    continue
                if nei in seen:
                    return False
                result = dfs(nei, node)
                if not result:
                    return False
            return True
        
        return dfs(0, -1) and len(seen) == n