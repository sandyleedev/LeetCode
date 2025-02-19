class Solution:
    def romanToInt(self, s: str) -> int:
        # IV, IX, XL, XC, CD, CM
        if "IV" in s:
            s = s.replace("IV", "IIII")

        if "IX" in s:
            s = s.replace("IX", "VIIII")

        if "XL" in s:
            s = s.replace("XL", "XXXX")

        if "XC" in s:
            s = s.replace("XC", "LXXXX")

        if "CD" in s:
            s = s.replace("CD", "CCCC")

        if "CM" in s:
            s = s.replace("CM", "DCCCC")

        sum = 0

        for c in s:
            if c == "I":
                sum += 1
            if c == "V":
                sum += 5
            if c == "X":
                sum += 10
            if c == "L":
                sum += 50
            if c == "C":
                sum += 100
            if c == "D":
                sum += 500
            if c == "M":
                sum += 1000

        return sum