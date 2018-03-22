class Solution:
    def removeDuplicates(self, nums):
        i = 0
        while(i < len(nums) - 1):
            if (nums[i] == nums[i+1]):
                nums.pop(i)
            else:
                i += 1
        if len(nums) > 1:
            if nums[len(nums)-2] == nums[len(nums)-1]:
                nums.pop()
        return len(nums)