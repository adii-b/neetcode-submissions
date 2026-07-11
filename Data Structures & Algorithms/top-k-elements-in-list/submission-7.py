class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        freq_array = [[] for _ in range(len(nums) + 1)]
        hashmap = {}

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1

        for key in hashmap:
            freq_array[hashmap[key]].append(key)

        count = 0
        for i in range(len(freq_array) - 1, -1, -1):
            if count == k:
                return result
            if len(freq_array[i]) == 0:
                continue
            j = 0
            while j < len(freq_array[i]) and count < k:
                result.append(freq_array[i][j])
                j += 1
                count += 1

        return result
            