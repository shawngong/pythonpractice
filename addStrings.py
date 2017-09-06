class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        charArray = []
        i = len(num1) - 1
        j = len(num2) - 1
        carryOver = 0
        while i >= 0 or j >= 0:
            curVal = 0
            if i >= 0 and j >= 0:
                curVal += int(num1[i]) + int(num2[j])
                i -= 1
                j -= 1
            elif i >= 0:
                curVal += int(num1[i])
                i -= 1
            else: #j >= 0
                curVal += int(num2[j])
                j -= 1
            curVal += carryOver
            carryOver = curVal / 10
            charArray.append(str(curVal % 10))
        if carryOver == 1:
            charArray.append(str(1))
        charArray.reverse()
        return "".join(charArray)
