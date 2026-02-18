class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        ends = [intervals[0][1]]
        res = 0

        for start, end in intervals[1:]:
            if ends[0] > start:
                heapq.heappush(ends, end)
                res += 1
            else:
                heapq.heapreplace(ends, end)
        
        return len(ends)

        