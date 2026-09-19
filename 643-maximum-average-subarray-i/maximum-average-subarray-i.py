class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        a = sum(nums[:k])   #a, b= curr sum, max sum 
        b = a

        for i in range(k, len(nums)):
            a = a + nums[i] - nums[i - k]

            if a > b:
                b = a
        return b / k         
