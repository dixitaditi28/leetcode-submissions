class Solution:
    def maxScore(self, s: str) -> int:
        rightOnes = s.count('1')
        leftZeros = 0
        ans = 0

        for i in range(len(s) - 1):  # split before last char
            if s[i] == '0':
                leftZeros += 1
            else:
                rightOnes -= 1

            ans = max(ans, leftZeros + rightOnes)

        return ans