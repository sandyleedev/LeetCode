class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # either increasing or same
        # remove duplicate (twice is fine)
        # move the remaining in the first part of the array

        # do not allocate extra space
        # in-place

        mapp = defaultdict(int)

        for num in nums:
            if mapp[num] < 2:
                mapp[num] += 1

        k = 0

        for key, val in mapp.items():
            nums[k] = key

            if val == 2:
                k += 1
                nums[k] = key
            
            k += 1
        
        return k
