class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        x = len(nums)
        ans = [0] * (2 * x)

        for i, num in enumerate(nums):
            ans[i] = ans[i + x] = num

        return ans