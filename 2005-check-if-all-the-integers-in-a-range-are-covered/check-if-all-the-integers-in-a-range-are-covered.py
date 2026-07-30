class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        diff = [0] * 52

        for s, e in ranges:
            diff[s] += 1
            diff[e + 1] -= 1

        active_ranges = 0
        for i in range(1, 51):
            active_ranges += diff[i]

            if left <= i <= right and active_ranges == 0:
                return False
        return True        