class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # down (m - 1) time(s)
        # right (n - 1) time(s)

        # down 2 times
        # right 6 times

        # [] [] [] [] [] [] [] []

        # (8 * 7) / 2

        # down down

        # 56 / 2 = 28

        # =================
        # [] [] []
        # down 2 times
        # right 1 time

        # (3 * 2) / 2


        total_slots = (m - 1) + (n - 1)
        print(total_slots)

        mul = 1
        for i in range(0, m - 1):
            mul *= total_slots - i
            mul //= (i + 1)

        return mul




