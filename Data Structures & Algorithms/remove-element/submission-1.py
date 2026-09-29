class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        corrected = []

        for num in nums:
            if num != val:
                corrected.append(num)
        
        for i in range(0, len(nums)):
            if i < len(corrected):
                nums[i] = corrected[i]
            else:
                nums[i] = 0
    
        return len(corrected)