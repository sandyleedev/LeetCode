class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # use binary search
        left = 1
        right = num

        while left <= right:
            m = int((left + right) / 2)
            m2 = m * m

            if m2 == num:
                return True
            elif m2 < num:
                left = m + 1
            elif m2 > num:
                right = m - 1


        return False