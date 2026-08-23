class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result = []
        elem1, elem2, cnt1, cnt2 = -1, -1, 0, 0

        for num in nums:
            if num == elem1:
                cnt1 += 1
            elif num == elem2:
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

        cnt1, cnt2 = 0, 0
        for num in nums:
            if num == elem1:
                cnt1 += 1
            elif num == elem2:
                cnt2 += 1

        if cnt1 > len(nums) // 3:
            result.append(elem1)
        if cnt2 > len(nums) // 3:
            result.append(elem2)

        return result