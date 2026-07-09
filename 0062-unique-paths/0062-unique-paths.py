class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        total_slots = (m - 1) + (n - 1)

        mul = 1
        for i in range(0, m - 1):
            mul *= total_slots - i
            mul //= (i + 1)

        return mul