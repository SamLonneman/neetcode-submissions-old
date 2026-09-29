class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Translate a number to a matrix: 12 slots: 7 translates to matrix[7//4][7%4]
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = m * n - 1
        while l <= r:
            mid = l + (r - l) // 2
            mid_element = matrix[mid//n][mid%n]
            if mid_element > target:
                r = mid - 1
            elif mid_element < target:
                l = mid + 1
            else:
                return True
        return False
