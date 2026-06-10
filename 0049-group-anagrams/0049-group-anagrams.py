class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()

        for s in strs:
            sstr = "".join(sorted(s))
            if sstr in d:
                d[sstr].append(s)
            else:
                d[sstr] = [s]
        
        output = []
        for v in d.values():
            output.append(v)
        
        return output