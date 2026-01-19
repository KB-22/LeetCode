class Solution:
    def maxSideLength(self, mat, threshold):
        m, n = len(mat), len(mat[0])

        # Step 1: Build prefix sum matrix
        prefix = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix[i][j] = (
                    mat[i - 1][j - 1]
                    + prefix[i - 1][j]
                    + prefix[i][j - 1]
                    - prefix[i - 1][j - 1]
                )

        # Step 2: Try all square sizes
        ans = 0
        max_len = min(m, n)

        for k in range(1, max_len + 1):
            found = False
            for i in range(k, m + 1):
                for j in range(k, n + 1):
                    square_sum = (
                        prefix[i][j]
                        - prefix[i - k][j]
                        - prefix[i][j - k]
                        + prefix[i - k][j - k]
                    )
                    if square_sum <= threshold:
                        found = True
                        break
                if found:
                    break
            if found:
                ans = k
            else:
                break

        return ans
