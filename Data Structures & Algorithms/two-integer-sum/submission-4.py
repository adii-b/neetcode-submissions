class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq_map = {}

        for i in range(len(nums)):
            num = target - nums[i]
            if num in freq_map:
                return [freq_map[num], i]
            else:
                freq_map[nums[i]] = i
        
        return []