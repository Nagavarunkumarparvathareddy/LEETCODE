class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        ans = []
        res = []
        arr = []
        for ele in image:
            ans.append(ele[::-1])
        flipped_arr = [[1 - element for element in row] for row in ans]
        return flipped_arr