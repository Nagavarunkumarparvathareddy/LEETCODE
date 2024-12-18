class Solution(object):
    def smallestNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        while(True):
            b = str(bin(n))[2:]
            l = len(b)
            lst = list(b)
            c = lst.count('1')
            if c == l:
                return int(str(b),2)
            else:
                n += 1