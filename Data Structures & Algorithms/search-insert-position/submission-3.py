class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        # last_move = None
        while l <= r:
            mid = (r + l) // 2
            print(mid, nums[mid])
            
            print(l, r)
            print("-")
            if nums[mid] > target:
                r = mid - 1
                # last_move = "-"
            elif nums[mid] < target:
                l = mid + 1
                # last_move = "+"
            else:
                return mid
        return l