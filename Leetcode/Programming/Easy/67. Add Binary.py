class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        n1 = int(a,2)
        n2 = int(b,2)
        ans = n1+n2
        return str(bin(ans))[2:]