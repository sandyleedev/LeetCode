class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        res = 1
        intervals.sort()
        ends = [intervals[0][1]]

        for start, end in intervals[1:]:
            if min(ends) <= start:
                ends.remove(min(ends))
            else:
                res += 1
            ends.append(end)
        
        return res