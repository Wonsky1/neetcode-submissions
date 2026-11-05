class Solution:
    def return_index_if_target(self, l, r, mid, target, nums: list) -> int:
        if nums[mid] == target:
            return mid
        if nums[l] == target:
            print("found")
            return l
        if nums[r] == target:
            print("found")
            return r
        return -1
    
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l<=r:

            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # Right half is sorted
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        print(l, r)
        return -1