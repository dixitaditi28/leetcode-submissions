class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if not nums:
            return[-1, -1]

        def lowerBound (nums, target):
            n = len(nums)
            lb = n
            l = 0
            h = n-1

            while l <= h:
                m = (l + h)//2
                if nums[m]>= target:
                    lb = m
                    h = m - 1
                else: 
                    l = m + 1
            return lb

        def upperBound (nums, target):
            n = len(nums)
            ub = n
            l = 0
            h = n - 1
            while l <= h:
                m = (l+h)//2
                if nums[m]> target:
                    ub = m
                    h = m - 1
                else:
                    l = m + 1
            return ub

        lb = lowerBound(nums, target)

        if lb == len(nums) or nums[lb] != target:
            return [-1, -1]
        ub = upperBound(nums, target)

        return [lb, ub-1]        


      
