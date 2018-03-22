class Solution:
    def summaryRanges(self, nums):
        List = []
        Output = []
        for i in range(len(nums)):
            value = nums[i]
            List.append(value)   
            if (i == (len(nums) - 1) or (nums[i+1] - value) != 1):
                if len(List) > 1:
                    s = str(List[0]) + "->" + str(List[len(List) - 1])
                else:
                    s = str(List[0])
                Output.append(s)
                List = []
        return Output