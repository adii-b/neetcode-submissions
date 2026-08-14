class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums_set = set(nums)

        for num in nums_set:
            if num - 1 not in nums_set:
                cur_seq = 1
                cur_elem = num
                while cur_elem + 1 in nums_set:
                    cur_seq += 1
                    cur_elem += 1
                longest = max(longest, cur_seq)
        
        return longest