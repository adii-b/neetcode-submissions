class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(nums):
            if len(nums) <= 1:
                return nums
            
            midIdx = len(nums) // 2
            left = nums[:midIdx]
            right = nums[midIdx:len(nums)]

            l = mergeSort(left)
            r = mergeSort(right)
            return merge(l, r)
        
        def merge(left, right):
            i, j = 0, 0
            finalArray = []

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    finalArray.append(left[i])
                    i += 1
                else:
                    finalArray.append(right[j])
                    j += 1
            
            while i < len(left):
                finalArray.append(left[i])
                i += 1
            
            while j < len(right):
                finalArray.append(right[j])
                j += 1
        
            return finalArray

        return mergeSort(nums)