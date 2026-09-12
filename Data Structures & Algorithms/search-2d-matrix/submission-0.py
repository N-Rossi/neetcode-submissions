class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for arr in matrix:
            left, right = 0, len(arr) - 1
            if arr[right] == target:
                return True
            elif arr[right] < target:
                continue
            
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == target:
                    return True
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
        return False
        