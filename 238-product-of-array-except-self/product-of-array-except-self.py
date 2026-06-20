class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        l_product = 1
        for i in range (n):
            result[i] = l_product
            l_product *= nums[i]

        r_product = 1
        for i in range (n - 1, -1, -1):
            result[i] *= r_product
            r_product *= nums[i]

        return result         