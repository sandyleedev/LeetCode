class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for w in strs:
            key = "".join(sorted(w))
            d[key].append(w)
        
        return list(d.values())