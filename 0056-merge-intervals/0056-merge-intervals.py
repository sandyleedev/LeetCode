class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        if len(intervals) == 1:
            return intervals

        s = sorted(intervals, key = lambda x: x[0])
        merged = [s[0]]

        for i in range(1, len(s)):
            prev = merged[-1]       # 마지막으로 병합된 구간
            curr = s[i]

            if curr[0] <= prev[1]:
                prev[1] = max(prev[1], curr[1])
            else:
                merged.append(curr)
        
        return merged
