class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        majority = -1

        for num in nums:
            if cnt == 0:
                majority = num
                cnt = 1
            elif majority == num:
                cnt += 1
            else:
                cnt -= 1
        
         
        return majority