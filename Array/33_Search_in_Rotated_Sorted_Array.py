class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        mid = 0
        while(start <= end):
            mid = int((start + end) / 2)
            if(nums[mid] == target):
                return mid
            # 如果左半部分是有序的
            if(nums[start] <= nums[mid]):
                if(nums[start] <= target and target < nums[mid]):
                    end = mid - 1
                else:
                    start = mid + 1 
            # 如果右半部份是有序的
            else:
                if(nums[mid] < target and target <= nums[end]):
                    start = mid + 1
                else:
                    end = mid - 1
        #不满足min <= max条件时，返回-1
        return -1