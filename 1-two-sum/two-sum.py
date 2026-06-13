class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        h_map={}
        for i in range (0,n):
            remaining = target - nums[i]
            if remaining in h_map:
                return (h_map[remaining], i)
            h_map[nums[i]] =i          