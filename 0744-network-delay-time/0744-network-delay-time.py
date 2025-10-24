import heapq
from collections import defaultdict

class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """

        # graph - adjacency list {source: (target, weight)}
        # heap - heapq. (time to reach the node, node)
        # dist - distance time table

        # get the min heap
        # compare existing time in dist and new time
        # if inf still exists at the end, return -1

        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))
        
        dist = {i: float('inf') for i in range(1, n+1)}
        dist[k] = 0

        heap = [(0, k)]

        while heap:
            time, node = heapq.heappop(heap)

            if time > dist[node]:
                continue
            
            # enumerate neighbors
            for nxt, w in graph[node]:
                new_time = time + w
                if new_time < dist[nxt]:
                    dist[nxt] = new_time
                    heapq.heappush(heap, (new_time, nxt))
        
        ans = max(dist.values())
        if ans != float('inf'):
            return ans
        else:
            return -1
    

