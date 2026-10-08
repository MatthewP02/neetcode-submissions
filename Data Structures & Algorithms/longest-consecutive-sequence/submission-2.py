class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_len = 0

        for num in num_set:
            if num - 1 not in num_set:
                new_len = 1
                curr = num

                while curr + 1 in num_set:
                    curr += 1
                    new_len += 1
                
                max_len = max(max_len, new_len)
        
        return max_len