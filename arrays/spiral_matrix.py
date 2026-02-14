'''leetcode 54 - spiral matrix

given an m * n matrix, return all elements of elements of the matrix in spiral order.

Example:
input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
output: [1,2,3,6,9,8,7,4,5]


Time Complexity: O(m * n)
Space Complexity: O(1) (excluding output list)

'''

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        result = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        while top <= bottom and left <= right:
            # Traverse from left to right
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1
            
            # Traverse from top to bottom
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1
            
            if top <= bottom:
                # Traverse from right to left
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1
            
            if left <= right:
                # Traverse from bottom to top
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1
        
        return result

# Example
if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    sol = Solution()
    print(sol.spiralOrder(matrix))
