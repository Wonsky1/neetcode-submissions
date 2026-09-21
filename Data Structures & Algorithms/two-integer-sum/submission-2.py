class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        set_nums = set(nums)
        seen = {}

        for index, item in enumerate(nums):
            print(item, index)
            needed = target - item
            if needed in seen:
                return [seen[needed], index]
            seen[item] = index
        return []