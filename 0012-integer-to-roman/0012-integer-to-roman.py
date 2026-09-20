class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""

        while 1000 <= num:
            num -= 1000
            res += "M"
        
        if 900 <= num:
            num -= 900
            res += "CM"

        if 500 <= num:
            num -= 500
            res += "D"
        
        if 400 <= num:
            num -= 400
            res += "CD"
        
        while 100 <= num:
            num -= 100
            res += "C"
        
        if 90 <= num:
            num -= 90
            res += "XC"
        
        if 50 <= num:
            num -= 50
            res += "L"
        
        if 40 <= num:
            num -= 40
            res += "XL"
        
        while 10 <= num:
            num -= 10
            res += "X"
        
        if 9 <= num:
            num -= 9
            res += "IX"
        
        if 5 <= num:
            num -= 5
            res += "V"
        
        if 4 <= num:
            num -= 4
            res += "IV"
        
        while 1 <= num:
            num -= 1
            res += "I"

        return res


