class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        max_res = 0

        for i in nums:
            if i == 0:
                res = 0
            elif i == 1:
                res += 1
                if res > max_res:
                    max_res = res

        return max_res