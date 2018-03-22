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

"""public int removeDuplicates(int[] nums) {
    if (nums.length == 0) return 0;
    int i = 0;
    for (int j = 1; j < nums.length; j++) {
        if (nums[j] != nums[i]) {
            i++;
            nums[i] = nums[j];
        }
    }
    return i + 1;
}"""