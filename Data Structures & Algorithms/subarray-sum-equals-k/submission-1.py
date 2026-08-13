class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash_map = {0: 1}
        c = 0

        prefix_sum = [nums[0]]

        for i in range(1, len(nums)):
            prefix_sum.append(nums[i] + prefix_sum[i - 1])

        for num in prefix_sum:
            x = num - k
            if x in hash_map:
                c += hash_map[x]
            hash_map[num] = hash_map.get(num, 0) + 1
        return c 
