class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_arr = [nums[0]]
        for i in range(1, len(nums)):
            prefix_arr.append(prefix_arr[i - 1] + nums[i])
        
        h_map = {0: 1}
        count = 0

        for i in range(len(nums)):
            if prefix_arr[i] - k in h_map:
                count += h_map[prefix_arr[i] - k]
            h_map[prefix_arr[i]] = h_map.get(prefix_arr[i], 0) + 1
        
        return count