class Solution:
    def twoSum(self, numbers, target):
        length = len(numbers)
        index1 = 0
        index2 = length - 1
        while (index1 != index2):
            first = numbers[index1]
            second = numbers[index2]
            Sum = first + second
            if (Sum == target):
                return (index1+1, index2+1)
            elif (Sum > target):
                index2 -= 1
            else:
                index1 += 1