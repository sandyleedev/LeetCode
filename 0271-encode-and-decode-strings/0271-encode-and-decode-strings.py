class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = []
        # 5#hello4#code
        for s in strs:
            res.append(str(len(s)) + "#" + s)
        return "".join(res)
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        # 5#hello4#code
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            i = j + length + 1
        return res

        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))