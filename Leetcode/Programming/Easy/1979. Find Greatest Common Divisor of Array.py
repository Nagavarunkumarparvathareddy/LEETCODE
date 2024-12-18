class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = max(nums)
        l = min(nums)
        for i in range(m, 0, -1):
            if m % i == 0 and l % i == 0:
                return i
                break
