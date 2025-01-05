class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        ans = letters[0]
        unique_letters = sorted(list(set(letters)))
        for ele in unique_letters:
            if ele > target:
                ans = ele
                break
        return ans
