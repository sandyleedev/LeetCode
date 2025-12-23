class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}      # key: number, value: index

        for i, num in enumerate(nums):
            num2 = target - num
            if num2 in d:
                return [i, d[num2]]
            else:
                d[num] = i