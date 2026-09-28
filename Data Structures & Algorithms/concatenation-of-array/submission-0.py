class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []

        for a in range(2):
            ans.extend(nums)
        
        return ans