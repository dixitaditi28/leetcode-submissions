class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c=0
        m_c=0

        for i in range (0, len(nums)):
            if nums[i] ==1:
                c+=1
            else:
                m_c= max(m_c,c)
                c = 0

        return max(m_c, c)            