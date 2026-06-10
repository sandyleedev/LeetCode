class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = dict()

        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
        for j in t:
            if j not in d:
                return False
            if d[j] > 1:
                d[j] -= 1
            elif d[j] == 1:
                del d[j]
        
        # if there's a remaining letter in d
        return not d