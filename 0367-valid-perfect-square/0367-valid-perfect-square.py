class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1

        while (i <= num):
            if i*i == num:
                return True
            elif i*i > num:
                return False 
            i += 1