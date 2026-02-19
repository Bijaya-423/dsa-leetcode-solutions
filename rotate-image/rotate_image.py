"""
LeetCode 48 - Rotate Image

Problem:
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).

IMPORTANT:
- You must rotate the matrix in-place.
- Do NOT use another 2D matrix.

Approach:
1. Transpose the matrix (swap rows with columns)
2. Reverse each row

"""

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in matrix:
            row.reverse()

#example
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print("Original Matrix 1:")
    for row in matrix1:
        print(row)

    sol.rotate(matrix1)

    print("\nRotated Matrix 1:")
    for row in matrix1:
        print(row)

    print("\n" + "="*40)

    # Example 2
    matrix2 = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]

    print("Original Matrix 2:")
    for row in matrix2:
        print(row)

    sol.rotate(matrix2)

    print("\nRotated Matrix 2:")
    for row in matrix2:
        print(row)
