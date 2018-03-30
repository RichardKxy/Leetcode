class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        Sum = 1
        carry = 0
        for i in range(len(digits)-1,-1,-1):
            Sum += (digits[i] + carry)
            carry = int(Sum / 10)
            digits[i] = Sum % 10
            Sum = 0
        if carry != 0:
            digits.insert(0,1)
        return digits