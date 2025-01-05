class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s = list(set(nums))
        for ele in s:
            if nums.count(ele) > len(nums)/2:
                return ele