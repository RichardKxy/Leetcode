class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        """l = g = -float('inf')
        for n in nums:
            l = max(n,l+n)
            g = max(l,g)
        return g
        """
        msum = nums[0]
        current_sum = 0
        for num in nums:
            current_sum += num
            if msum < current_sum:
                msum = current_sum
            if current_sum < 0:
                current_sum = 0
                continue
        return msum    
        