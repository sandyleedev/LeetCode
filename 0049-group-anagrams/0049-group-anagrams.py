class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        # key: sorted string / value: str array

        for s in strs:
            # sstr = sorted(s).join("")
            sstr = "".join(sorted(s))
            if sstr in d:
                d[sstr].append(s)
            else:
                d[sstr] = [s]
        
        output = []
        for v in d.values():
            output.append(v)
        
        return output