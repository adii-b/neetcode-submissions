class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}

        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1
        
        for key in hash_map:
            if hash_map[key] > 1:
                return True
        
        return False