class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        val_to_idx = {x: index for index, x in enumerate(arr)}
        dp = {}
        max_len = 0

        n = len(arr)
        for j in range(n):
            for i in range(j):
                prev_val = arr[j] - arr[i]

                if prev_val in val_to_idx and prev_val < arr[i]:
                    k = val_to_idx[prev_val]
                    dp[i, j] = dp.get((k, i), 2) + 1
                    max_len = max(max_len, dp[i, j])
        return max_len if max_len >= 3 else 0