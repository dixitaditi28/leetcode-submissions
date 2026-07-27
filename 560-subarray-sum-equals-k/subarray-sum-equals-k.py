class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c = 0
        curr_sum = 0

        pre_map = {0 : 1}

        for num in nums:
            curr_sum += num

            if curr_sum - k in pre_map:
                c += pre_map[curr_sum - k]

            pre_map[curr_sum] = pre_map.get(curr_sum, 0) + 1
        return c         
        