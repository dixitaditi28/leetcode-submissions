class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        a = []      # result
        b = []      # current subset

        def backtrack(ind):
            if ind == len(nums):
                a.append(b.copy())
                return

           
            backtrack(ind + 1)

            b.append(nums[ind])
            backtrack(ind + 1)
            b.pop()

        backtrack(0)
        return a
