class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_s= nums[0]
        max_s= nums[0]

        for i in range (1, len(nums)):
            current_s = max(current_s +nums[i], nums[i])
            max_s = max(current_s, max_s)
        return max_s    