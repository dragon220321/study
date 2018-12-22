class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            x = str(x)[::-1]
        else:
            temp = str(x)[::-1]
            x = "-" + temp[:(len(temp)-1)]
        x = int(x)
        if -2**31 <= x <= 2**31 - 1:
            return x
        return 0

test = Solution()
a = -3460
a = print(test.reverse(a))