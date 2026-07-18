class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        adj = [[] for _ in range(n)]
        for A, B in edges:
            adj[A].append(B)
            adj[B].append(A)
        
        parent = {0: -1}
        stack = [0]

        while stack:
            node = stack.pop()
            for nei in adj[node]:
                if nei == parent[node]:
                    continue
                if nei in parent:
                    return False
                stack.append(nei)
                parent[nei] = node
        
        return len(parent) == n