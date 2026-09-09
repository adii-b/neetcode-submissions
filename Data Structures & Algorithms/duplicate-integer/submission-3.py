class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq_map = {}

        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        for key in freq_map:
            if freq_map[key] > 1:
                return True
        
        return False