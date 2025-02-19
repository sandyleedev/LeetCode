class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s) == 1:
            return 0

        non_unique_set = set()

        for i in range(len(s) - 1):
            if s.find(s[i], i + 1) == -1 and s[i] not in non_unique_set:
                return i
            else:
                non_unique_set.add(s[i])
        
        # last char
        if s[len(s) - 1] not in non_unique_set:
            return len(s) - 1
        
        return -1