class Codec:
    def encode(self, strs: List[str]) -> str:
        res = []
        for w in strs:
            res.append(str(len(w)) + "#" + w)
        return "".join(res)
        
    
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        # 5#hello4#code
        
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            # if j == "#"
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            i = j + 1 + length
        
        return res