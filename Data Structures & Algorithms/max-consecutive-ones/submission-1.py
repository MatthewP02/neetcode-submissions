class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        max_res = 0

        for i in nums:
            if i == 0:
                res = 0
            elif i == 1:
                res += 1
                max_res = max(res, max_res)

        return max_res