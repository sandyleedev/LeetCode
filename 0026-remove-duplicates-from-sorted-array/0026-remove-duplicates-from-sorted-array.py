class Solution(object):
    def removeDuplicates(self, nums) :
        result = []
        k = 0

        for i in range(len(nums)):
            if (nums[i] not in result):
                result.append(nums[i])
                k += 1
            elif (nums[i] in result):
                nums[i] = "_"

        nums.sort(key=lambda x: (isinstance(x, str), x))
        
        return k