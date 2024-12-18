class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle not in haystack :
            return -1
        if len(needle)> len(haystack):
            return -1
        else:
            l1 = len(haystack)
            l2 = len(needle)
            iter = (l1-l2)+1
            i = 0
            a = 0
            b = l2
            while (i< iter):
                if haystack[a:b] == needle:
                    ans = i
                    break
                i += 1
                a+= 1
                b += 1
            return ans


