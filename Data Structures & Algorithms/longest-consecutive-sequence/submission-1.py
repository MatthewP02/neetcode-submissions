class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_len = 0

        for num in num_set:
            if num - 1 not in num_set:
                new_len = 1
                for i in range(1, len(num_set)):
                    if num+i in num_set:
                        new_len += 1
                    else:
                        break
                
                max_len = max(max_len, new_len)
        
        return max_len