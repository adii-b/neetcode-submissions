class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        long_seq = 0
        for num in nums:
            temp = num
            if num - 1 not in nums_set:
                cur_seq = 1
                while temp + 1 in nums_set:
                    cur_seq += 1
                    temp += 1
                long_seq = max(cur_seq, long_seq)
        
        return long_seq