class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 2

        if n == 1:
            return 1
        if n == 2:
            return 2

        res = 0

        for i in range(3, n + 1):
            res = one + two
            one = two
            two = res

        return res