class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []
        inserted = False
        
        newStart, newEnd = newInterval[0], newInterval[1]

        for start, end in intervals:
            if inserted:
                if output[-1][1] < start:
                    output.append([start, end])
                else:
                    output[-1] = [min(output[-1][0], start), max(output[-1][1], end)]
            else:
                if newEnd < start:
                    output.append(newInterval)
                    output.append([start, end])
                    inserted = True
                else:
                    if end < newStart:
                        output.append([start, end])
                    else:
                        output.append([min(start, newStart), max(end, newEnd)])
                        inserted = True

        if not inserted:
            output.append(newInterval)
        
        return output