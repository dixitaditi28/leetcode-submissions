class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        nums = [int(x) for x in s]
        count = 0

        for i in range(n - 1):
            cZ = nums[:i+1].count(0)
            cO = nums[i+1:].count(1)
            count = max(count, cZ + cO)

        return count           
        