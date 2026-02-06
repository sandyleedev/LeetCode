class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []

        if not intervals:
            output.append(newInterval)

        for index, i in enumerate(intervals):
            # if newInterval is already in the output array
            if newInterval in output:
                output.append(i)
                continue

            # non-overlapping
            if newInterval[1] < i[0] or newInterval[0] > i[1]:
                if i[0] < newInterval[0]:
                    output.append(i)
                    if index == len(intervals) - 1:
                        output.append(newInterval)
                else:
                    output.append(newInterval)
                    output.append(i)
            # overlapping -> need to merge
            else:
                start = min(i[0], newInterval[0])
                end = max(i[1], newInterval[1])
                newInterval = [start, end]
                if index == len(intervals) - 1:
                    output.append(newInterval)

        return output