import heapq
from collections import defaultdict

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        
        # flights = [from, to, price] [u, v, w]
        # cheapest price from src to dst with at most k steps

        graph = defaultdict(list)

        for u, v, w in flights:
            graph[u].append((v, w))

        # dist[node][stops] = cost
        dist = [[float('inf')] * (k+2) for _ in range(n)]
        dist[src][0] = 0

        # price to the node, node, stops
        heap = [(0, src, 0)]

        while heap:
            price, node, stops = heapq.heappop(heap)

            if node == dst:
                return price
            
            if stops == k + 1:
                continue
            
            # look at the neighbors
            for nxt, p in graph[node]:
                new_price = price + p
                if new_price < dist[nxt][stops+1]:
                    dist[nxt][stops+1] = new_price
                    heapq.heappush(heap, (new_price, nxt, stops + 1))
        
        return -1