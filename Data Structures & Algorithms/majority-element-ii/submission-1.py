class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt1, cnt2, elem1, elem2 = 0, 0, -1, -1
        result = []

        for num in nums:
            if elem1 == num:
                cnt1 += 1
            elif elem2 == num:
                cnt2 += 1
            elif cnt1 == 0:
                elem1 = num
                cnt1 = 1
            elif cnt2 == 0:
                elem2 = num
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        
        cnt1 = sum(1 for num in nums if num == elem1)
        cnt2 = sum(1 for num in nums if num == elem2)
        
        if cnt1 > len(nums) // 3:
            result.append(elem1)
        if cnt2 > len(nums) // 3 and elem1 != elem2:
            result.append(elem2)
        
        return result
            