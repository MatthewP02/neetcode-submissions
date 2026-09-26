class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index, value in enumerate(nums):
            goal = target - value
            if goal in seen:
                return [seen[goal], index]

            seen[value] = index