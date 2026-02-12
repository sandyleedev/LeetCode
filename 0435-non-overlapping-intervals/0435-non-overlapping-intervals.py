class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        output = 0
        prev_index = 0

        for i in range(1, len(intervals)):
            prev = intervals[prev_index]
            curr = intervals[i]

            if prev[1] <= curr[0]:
                prev_index = i
                continue
            else:
                output += 1
                if prev[1] > curr[1]:
                    prev_index = i

        return output