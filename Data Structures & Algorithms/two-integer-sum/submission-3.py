class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h_map = {}

        for i in range(len(nums)):
            num = target - nums[i]
            if num in h_map:
                return [h_map[num], i]
            else:
                h_map[nums[i]] = i
            
        
