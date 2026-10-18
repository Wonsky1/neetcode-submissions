class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l=0
        r=0
        current_window = set()
        # prev_window = set()
        while r < len(nums):
            print("current cycle: ", r, nums[r])
            if nums[r] in current_window:
                return True
            current_window.add(nums[r])
            r += 1
            if r - l > k:
                current_window.remove(nums[l])
                l += 1

            # l = l + 1 if r - l > k else l
        return False
            
