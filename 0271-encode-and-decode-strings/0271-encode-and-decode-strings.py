class Codec:
    def encode(self, strs: List[str]) -> str:
        res = []
        for w in strs:
            res.append(str(len(w)) + "#" + w)
        return "".join(res)
        
    
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0       # current delimeter index
        
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1                
            # char is not #
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            i = j + length + 1
        return res

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))