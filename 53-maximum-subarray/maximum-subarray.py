class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = nums[0]
        max_s= nums[0]

        for i in range (1, len(nums)):
            curr = max(curr +nums[i], nums[i])
            max_s = max(curr, max_s)
        return max_s    