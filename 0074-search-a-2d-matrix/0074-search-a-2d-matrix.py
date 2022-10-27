class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        if n == 0:
            return False
        
        m = len(matrix[0])
        
        lo, hi = 0, n*m-1
        
        while lo <= hi:
            
            mid = lo + (hi - lo) // 2
            
            if target == matrix[mid // m][mid % m]:
                return True
            
            elif target < matrix[mid // m][mid % m]:
                hi = mid - 1
            
            else:
                lo = mid + 1
        
        return False