class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        
        output = [intervals[0]]

        for start, end in intervals[1:]:
            prev_start = output[-1][0]
            prev_end = output[-1][1]

            if start <= prev_end:
                output[-1] = [min(start, prev_start), max(end, prev_end)]
            else:
                output.append([start, end])
        
        return output