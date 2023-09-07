class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1
        while l <= r:
            mid = (l + r) // 2
            if target < matrix[mid][0]:
                r = mid - 1
            elif target > matrix[mid][-1]:
                l = mid + 1
            else:
                break
        if l <= r:
            row = (l + r) // 2
            l, r = 0, len(matrix[row])-1
            while l <= r:
                mid = (l + r) // 2
                if target < matrix[row][mid]:
                    r = mid - 1
                elif target > matrix[row][mid]:
                    l = mid + 1
                else:
                    return True
        return False
