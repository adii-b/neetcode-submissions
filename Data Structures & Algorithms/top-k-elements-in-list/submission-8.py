class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in  range(len(nums) + 1)] 
        result = []
        hash_map = {} 

        for num in nums:
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1


        for key in hash_map:
            bucket[hash_map[key]].append(key)
        
        for b in reversed(bucket):
            for i in range(len(b)):
                if len(result) == k:
                    break
                result.append(b[i])
        
        return result
            

