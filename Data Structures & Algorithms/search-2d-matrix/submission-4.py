class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        while l <= r:
            mid = (l + r) // 2
            print(mid)
            if matrix[mid][-1] > target:
                print("mid > target")
                if mid == 0 or matrix[mid][0] <= target:
                    print("1")
                    for item in matrix[mid]:
                        if item == target:
                            return True
                    return False
                r = mid - 1
            elif matrix[mid][-1] < target:
                print("mid < target")
                if mid == len(matrix) - 1:
                    print("1")
                    for item in matrix[mid]:
                        if item == target:
                            return True
                l = mid + 1
            else:
                return True

        return False