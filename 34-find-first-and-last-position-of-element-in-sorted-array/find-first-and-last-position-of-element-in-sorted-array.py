class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def get_first(t: int) -> int:
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] < t:
                    l = mid + 1
                else: 
                    r = mid - 1
            return l

        left_ind = get_first(target)
        if left_ind == len(nums) or nums[left_ind] != target:
            return [-1, -1]

        right_ind = get_first(target + 1) - 1

        return [left_ind, right_ind]                    
