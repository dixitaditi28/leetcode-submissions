class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        curr = 0
        rem_map = {0 : -1}

        for i, num in enumerate(nums):
            curr += num
            rem = curr % k

            if rem in rem_map:
                if i - rem_map[rem] >= 2:
                    return True
            else:
                rem_map[rem] = i
        return False                