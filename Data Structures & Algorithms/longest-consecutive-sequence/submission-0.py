class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_set = set(nums)
        longest = 1
        for item in nums_set:
            if item - 1 in nums_set:
                continue
            current_longest = 1
            next_item = item + 1
            while next_item in nums_set:
                current_longest += 1
                next_item += 1
            if current_longest > longest:
                longest = current_longest
        return longest

        