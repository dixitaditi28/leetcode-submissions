class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        mySet = set(nums)
        longest =0
        
        for num in mySet:
            if num-1 not in mySet:
                x=num
                count = 1
                while x+1 in mySet:
                    count+=1
                    x+=1
                longest = max(longest,count)
        return longest