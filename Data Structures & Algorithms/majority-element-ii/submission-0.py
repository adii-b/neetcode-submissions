class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        # First Pass: Find potential candidates
        elem1, elem2 = None, None
        cnt1, cnt2 = 0, 0

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

        # Second Pass: Verify actual frequencies
        res = []
        threshold = len(nums) // 3

        for candidate in (elem1, elem2):
            if candidate is not None and nums.count(candidate) > threshold:
                res.append(candidate)

        return res      