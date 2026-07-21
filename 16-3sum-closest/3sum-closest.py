class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('inf')

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums [i-1]:
                if i> 0 and nums[i] ==  nums[i-1]:
                    continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                currsum = nums[i] + nums[l] + nums[r]

                if currsum == target:
                    return currsum

                if abs(currsum - target) < abs (closest - target):
                    closest = currsum

                if currsum > target:
                    r -= 1
                else: 
                    l += 1
        return closest                               
