class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1
        x = abs(x)
        revNum = 0

        while x != 0:
            ld = x % 10
            revNum = revNum * 10 + ld
            x = x // 10

        revNum *= sign

        # 32-bit signed integer range check
        if revNum < -2**31 or revNum > 2**31 - 1:
            return 0
        return revNum
