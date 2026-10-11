class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            current_mid_item = nums[mid]
            # print(f"""
            # mid={mid}={current_mid_item}
            # left={left}
            # right={right}
            # """)
            if current_mid_item > target:
                right = mid - 1
            elif current_mid_item < target:
                left = mid + 1
            else:
                return mid
        return -1