class Solution:
    def trailingZeroes(self, n: int) -> int:
        z_count = 0

        while n > 0:
            n = n// 5
            z_count += n     
        return z_count    