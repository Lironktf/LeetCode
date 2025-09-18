class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        cur = 0

        for i in range(len(s) - 1):            
            after = 0

            if s[i] == "I": cur = 1
            elif s[i] == "V": cur = 5
            elif s[i] == "X": cur = 10
            elif s[i] == "L": cur = 50
            elif s[i] == "C": cur = 100
            elif s[i] == "D": cur = 500
            elif s[i] == "M": cur = 1000

            if s[i+1] == "I": after = 1
            elif s[i+1] == "V": after = 5
            elif s[i+1] == "X": after = 10
            elif s[i+1] == "L": after = 50
            elif s[i+1] == "C": after = 100
            elif s[i+1] == "D": after = 500
            elif s[i+1] == "M": after = 1000

            1000 + 900
            if after > cur:
                total += after-cur
                i += 1
            else:
                total += cur

        return total + cur


        