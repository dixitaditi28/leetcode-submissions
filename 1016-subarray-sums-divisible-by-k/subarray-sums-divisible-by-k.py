class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        c = 0
        curr_sum = 0

        rem_map = {0: 1}

        for num in nums:
            curr_sum += num 
            rem = curr_sum % k

            if rem in rem_map:
                c += rem_map[rem]

            rem_map[rem] = rem_map.get(rem, 0) + 1

        return c        