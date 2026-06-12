class Solution:
    def maxScore(self, s: str) -> int:
        max_s = 0
        z = 0
        ones = s.count('1')
        for i in range(len(s) - 1):
            if s[i] == '0':
                z += 1
            else:
                ones -= 1
            max_s = max(max_s, z + ones)
        return max_s