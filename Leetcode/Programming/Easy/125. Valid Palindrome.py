class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        string = 'qwertyuioplkjhgfdsazxcvbnm0123456789'
        l = list(string)
        s = s.lower()
        inpstr = list(s)
        ans = ''
        for ele in inpstr:
            if ele in l:
                ans += ele
        if ans == ans[::-1]:
            return True
        return False


